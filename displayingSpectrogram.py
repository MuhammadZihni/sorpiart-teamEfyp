from twython import Twython
from tkinter import *
from tkinter import simpledialog
from time import gmtime, strftime
from pydub import AudioSegment
from matplotlib import pyplot as plot
from PIL import Image, ImageDraw, ImageFont
from subprocess import call 
import numpy as np
import os
import speech_recognition as sr
import sys
import time

src = "test.wav"
r = sr.Recognizer()

with sr.AudioFile(src) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text1 = r.recognize_google(audio_data)
    print(text1)
    
audio = AudioSegment.from_file(src)
data = np.frombuffer(audio._data, np.int16)
fs = audio.frame_rate

BARS = 500
BAR_HEIGHT = 300
LINE_WIDTH = 5

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

fnt = ImageFont.truetype('vcr.ttf', 50)

im = Image.new('RGB', (BARS * LINE_WIDTH, BAR_HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.text((0,0), text=text1 , font=fnt, fill=(0,0,0,255))


current_x = 1
for item in max_array:
    item_height = item/line_ratio

    current_y = (BAR_HEIGHT - item_height)/2
    draw.line((current_x, current_y, current_x, current_y + item_height), fill=(0, 0, 0), width=4)

    current_x = current_x + LINE_WIDTH

im.show()
main = Tk()
main.withdraw()
user_input = simpledialog.askstring(title="Get Name", prompt="Name:")


# filename = "audioSpec_" + strftime("%Y_%m_%d%H-%M-%S", gmtime()) + ".jpg"
# im.save("static/images/" + filename)

filename = "audioSpec" + ".jpg"
im.save("static/images/" + filename)


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
image = open('/home/pi/project/EGL314_Project_TeamC/static/images/audioSpec.jpg', 'rb')
response = twitter.upload_media(media=image)
media_id = [response['media_id']]
twitter.update_status(status=message, media_ids=media_id)


