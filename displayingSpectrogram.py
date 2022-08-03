from twython import Twython
from tkinter import *
from tkinter import simpledialog
from pydub import AudioSegment
from matplotlib import pyplot as plot
import matplotlib.image as mpimg
from PIL import Image, ImageDraw, ImageFont
from scipy.io import wavfile
import numpy as np
import speech_recognition as sr
import time

time.sleep(1)
samplingFrequency, signalData = wavfile.read('/home/pi/sorpiart-teamEfyp/Sound/wav/output.wav')  #for spectrogram
src = "/home/pi/sorpiart-teamEfyp/Sound/wav/output.wav"
r = sr.Recognizer()

#speech to text
with sr.AudioFile(src) as source:
    try:
    # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text1 = r.recognize_google(audio_data)
        print(text1)
    # when it deos not recognise anything, print ""
    except sr.UnknownValueError:
        text1 = ""
        print(text1)
    
audio = AudioSegment.from_file(src)
data = np.frombuffer(audio._data, np.int16)
fs = audio.frame_rate

BARS = 500
BAR_HEIGHT = 400
LINE_WIDTH = 4

length = len(data)
RATIO = length/BARS

count = 0
maximum_item = 0
max_array = []
highest_line = 0

for d in data:
    if count < RATIO:
        count = count + 1

        if abs(d) > maximum_item:
            maximum_item = abs(d)
    else:
        max_array.append(maximum_item)

        if maximum_item > highest_line:
            highest_line = maximum_item

        maximum_item = 0
        count = 1

line_ratio = highest_line/BAR_HEIGHT

# fnt = ImageFont.truetype('vcr.ttf', 50)
fnt = ImageFont.truetype("/home/pi/sorpiart-teamEfyp/vcr.ttf", 50)

im = Image.new('RGB', (BARS * LINE_WIDTH, BAR_HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.text((0,0), text=text1 , font=fnt, fill=(0,0,0,255))


current_x = 1
for item in max_array:
    item_height = item/line_ratio

    current_y = (BAR_HEIGHT - item_height)/2
    draw.line((current_x, current_y, current_x, current_y + item_height), fill=(0, 0, 0), width=5)

    current_x = current_x + LINE_WIDTH
    
filename = "audioSpec" + ".jpg" #save the bars diagram
im.save("/home/pi/sorpiart-teamEfyp/images/" + filename)

plot.subplot(211)
plot.title("waveform")
img = mpimg.imread('/home/pi/sorpiart-teamEfyp/images/audioSpec.jpg')
imgplot = plot.imshow(img)
    
plot.subplot(212)
plot.title("spectrogram")
plot.specgram(signalData,Fs=samplingFrequency)
bottom, top = plot.ylim()
left, right = plot.xlim()
plot.ylim(0, 10000)
plot.xlim(0, 4)
plot.xlabel('Time')
plot.ylabel('Frequency')
plot.savefig("/home/pi/sorpiart-teamEfyp/images/figure.jpg", bbox_inches="tight")  #save the plot which includes the spectrogra & bars diagrams

plot.show()  #plot.show() must be after plot.savefig beacuse polt.show() clears the plot

main = Tk()
main.withdraw()
user_input = simpledialog.askstring(title="Get Name", prompt="Name:")


from auth_twitter import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


message = user_input
image = open('/home/pi/sorpiart-teamEfyp/images/figure.jpg', 'rb')
response = twitter.upload_media(media=image)
media_id = [response['media_id']]
twitter.update_status(status=message, media_ids=media_id)



