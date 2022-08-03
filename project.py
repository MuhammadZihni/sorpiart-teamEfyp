from tkinter import *
import tkinter as tk
from tkinter import ttk
from pix2music import *
from tkinter import messagebox
from PIL import Image, ImageTk
import PIL.Image
from tkinter import font
import time
time.sleep(6)
from gtts import gTTS
import pygame
import speech_recognition as sr
from translate import Translator
from beatmaker import *
from recording_4_seconds import *
from tkinter.messagebox import Message

main = Tk()
main.geometry("1919x1150+0+0")
tabControl = ttk.Notebook(main)
pygame.mixer.init()


tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Music Maker")
tabControl.add(tab2, text="Record")
tabControl.add(tab3, text="Beat Maker")
tabControl.add(tab4, text="Translator")
tabControl.pack(expand=1, fill="both")  #expand = expand to fill any space not otherwise used. fill= fil space on x and y axis


row, col = 21, 18
notes=["Do","Re","Mi","Fa","So","La","Ti","Do","Re","Mi","Fa","So","La","Ti","Do","Re","Mi","Fa"]

FINISHED_RECORDING_MSG = "Finished Recording, Processing Now. Please Wait!"
FINISHED_RECORDING_DURATION = 3500

def click(i, j):
    global toggle
    if toggle[i][j] == 0:  
        if i == 0 or i == 11:
            toggle[i][j] = 1  
            button[i][j].config(bg="red")
        elif i == 1 or i == 12:
            toggle[i][j] = 1  
            button[i][j].config(bg="blue")
        elif i == 2 or i == 13:
            toggle[i][j] = 1  
            button[i][j].config(bg="green")
        elif i == 3 or i == 14:
            toggle[i][j] = 1  
            button[i][j].config(bg="yellow")
        elif i == 4 or i == 15:
            toggle[i][j] = 1  
            button[i][j].config(bg="orange")
        elif i == 5 or i == 16:
            toggle[i][j] = 1  
            button[i][j].config(bg="indigo")
        elif i == 6 or i == 17:
            toggle[i][j] = 1  
            button[i][j].config(bg="purple")
        elif i == 7 or i == 18:
            toggle[i][j] = 1  
            button[i][j].config(bg="cyan")
        elif i == 8 or i == 19:
            toggle[i][j] = 1  
            button[i][j].config(bg="maroon")
        elif i == 9 or i == 20:
            toggle[i][j] = 1  
            button[i][j].config(bg="gold")

    else:  
        toggle[i][j] = 0  
        button[i][j].config(bg="#CBC3E3")
    
    
def reset():
    global i,j
    profileClicked.set(profile[0])
    keyClicked.set(key[0])
    BPM_slider.set(60)
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="#CBC3E3")
            
def play():
    toggle, unselected
    print(toggle)
    if toggle==unselected:
        messagebox.showwarning("warning","Please select a note")
    else:
        pix2music(profileClicked.get(), BPM_slider.get(), keyClicked.get(), toggle)
        print("Profile is {}".format(profileClicked.get()))
        print("Key is {}".format(keyClicked.get()))
        print("BPM is {}".format(BPM_slider.get()))
        
    
def pix2music_instructions():
    messagebox.showinfo("Pix2music", "Step 1: Choose the key you want your music to be played at.\nC1(Lowest)-C6(Highest)\n\nStep 2: Choose the BPM (beats per minute).\n60(Slowest)-180(fastest)\n\nStep 3: Choose the different sound profiles.\ne.g. pluck\n\nStep 4: Choose the different notes to create your music.\ne.g. do, re, mi represented by the boxes on the left\n\nStep 5: Click on the play sound button to listen to the music you created.")


def Recording():
    record()
    pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/times_up.mp3") #Panda
    pygame.mixer.music.play()
    top = Toplevel()
    top.title("Recording")
    message = tk.Message(top, text=FINISHED_RECORDING_MSG, font = ("Flavors 100"), padx=500, pady=500)
    message.pack()
    top.after(FINISHED_RECORDING_DURATION, top.destroy)
    
       
def beatmaker_piano():
    piano()
    piano_label.config(fg="blue")
    drum_label.config(fg="black")
    print("piano mode activated")
    
def beatmaker_drums():
    drum()
    drum_label.config(fg="blue")
    piano_label.config(fg="black")
    
def beatmaker_instructions():
    messagebox.showinfo("Beatmaker", "Step 1: Choose either the Piano or Drums mode.\n\nStep 2: Click on the physical buttons to start producing sound")
    
    
def func(Value):
    global toggle
    if (Value == "1"):
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/turtle_sound.mp3") #Turtle
        pygame.mixer.music.play()
        for i in range(row):
            for j in range(col):
                button[i][j].config(bg="#CBC3E3")#turtle
        time.sleep(16)
        button[7][8].config(bg="dark green"), button[7][9].config(bg="dark green"), button[8][7].config(bg="dark green"), button[8][8].config(bg="dark green"), button[8][9].config(bg="dark green"), button[8][10].config(bg="dark green")
        button[9][6].config(bg="dark green"), button[9][7].config(bg="dark green"), button[9][8].config(bg="dark green"), button[9][9].config(bg="dark green"), button[9][10].config(bg="dark green"), button[9][11].config(bg="dark green")
        button[10][6].config(bg="dark green"), button[10][7].config(bg="dark green"), button[10][8].config(bg="dark green"), button[10][9].config(bg="dark green"), button[10][10].config(bg="dark green"), button[10][11].config(bg="dark green")
        button[11][6].config(bg="dark green"), button[11][7].config(bg="dark green"), button[11][8].config(bg="dark green"), button[11][9].config(bg="dark green"), button[11][10].config(bg="dark green"), button[11][11].config(bg="dark green")
        button[9][12].config(bg="light green"), button[9][13].config(bg="black"), button[9][14].config(bg="light green"), button[10][12].config(bg="light green"), button[10][13].config(bg="light green"), button[10][14].config(bg="light green")
        button[11][5].config(bg="light green"), button[12][6].config(bg="light green"), button[12][7].config(bg="light green"), button[12][8].config(bg="light green"), button[12][9].config(bg="light green"), button[12][10].config(bg="light green")
        button[12][11].config(bg="light green"), button[13][6].config(bg="light green"), button[13][7].config(bg="light green"), button[13][10].config(bg="light green"), button[13][11].config(bg="light green"), button[8][12].config(bg="light green")
        button[8][13].config(bg="light green")
        toggle = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        BPM_slider.set(180)
        profileClicked.set('triangle')
        keyClicked.set('C6')
    elif (Value == "2"):
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/duck_sound.mp3") #Duck
        pygame.mixer.music.play()
        for i in range(row):
            for j in range(col):
                button[i][j].config(bg="#CBC3E3")#duck
        time.sleep(10)
        button[4][7].config(bg="black"), button[4][8].config(bg="black"), button[4][9].config(bg="black"), button[5][6].config(bg="black"), button[5][10].config(bg="black"), button[6][4].config(bg="black"), button[6][5].config(bg="black")
        button[6][11].config(bg="black"), button[7][3].config(bg="black"), button[7][5].config(bg="black"), button[7][11].config(bg="black"), button[8][4].config(bg="black"), button[8][5].config(bg="black"), button[8][11].config(bg="black")
        button[9][6].config(bg="black"), button[9][10].config(bg="black"), button[10][7].config(bg="black"), button[10][8].config(bg="black"), button[10][9].config(bg="black"), button[11][6].config(bg="black"), button[11][10].config(bg="black")
        button[11][11].config(bg="black"), button[11][12].config(bg="black"), button[11][14].config(bg="black"), button[12][5].config(bg="black"), button[12][14].config(bg="black"), button[13][5].config(bg="black"), button[13][14].config(bg="black")
        button[14][5].config(bg="black"), button[14][14].config(bg="black"), button[15][6].config(bg="black"), button[15][13].config(bg="black"), button[16][7].config(bg="black"), button[16][8].config(bg="black"), button[16][9].config(bg="black")
        button[16][10].config(bg="black"), button[16][11].config(bg="black"), button[16][12].config(bg="black"), button[7][7].config(bg="black"), button[5][7].config(bg="yellow"), button[5][8].config(bg="yellow"), button[5][9].config(bg="yellow")
        button[6][6].config(bg="yellow"), button[6][7].config(bg="yellow"), button[6][8].config(bg="yellow"), button[6][9].config(bg="yellow"), button[6][10].config(bg="yellow"), button[7][6].config(bg="yellow"), button[7][7].config(bg="yellow")
        button[7][8].config(bg="yellow"), button[7][9].config(bg="yellow"), button[7][10].config(bg="yellow"), button[8][6].config(bg="yellow"), button[8][7].config(bg="yellow"), button[8][8].config(bg="yellow"), button[8][9].config(bg="yellow")
        button[8][10].config(bg="yellow"), button[9][7].config(bg="yellow"), button[9][8].config(bg="yellow"), button[9][9].config(bg="yellow"), button[11][7].config(bg="yellow"), button[11][8].config(bg="yellow"), button[11][9].config(bg="yellow"),
        button[11][13].config(bg="yellow"), button[12][6].config(bg="yellow"), button[12][7].config(bg="yellow"), button[12][8].config(bg="yellow"), button[12][9].config(bg="yellow"), button[12][10].config(bg="yellow"), button[12][11].config(bg="yellow")
        button[12][12].config(bg="yellow"), button[12][13].config(bg="yellow"), button[13][6].config(bg="yellow"), button[13][7].config(bg="yellow"), button[13][8].config(bg="yellow"), button[13][9].config(bg="yellow"), button[13][10].config(bg="yellow")
        button[13][11].config(bg="yellow"), button[13][12].config(bg="yellow"), button[13][13].config(bg="yellow"), button[14][6].config(bg="yellow"), button[14][7].config(bg="yellow"), button[14][8].config(bg="yellow"), button[14][9].config(bg="yellow")
        button[14][10].config(bg="yellow"), button[14][11].config(bg="yellow"), button[14][12].config(bg="yellow"), button[14][13].config(bg="yellow"), button[15][7].config(bg="yellow"), button[15][8].config(bg="yellow"), button[15][9].config(bg="yellow")
        button[15][10].config(bg="yellow"), button[15][11].config(bg="yellow"), button[15][12].config(bg="yellow"), button[10][13].config(bg="black"), button[7][7].config(bg="black"), button[7][4].config(bg="orange")
        toggle = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        BPM_slider.set(180)
        profileClicked.set('Sine')
        keyClicked.set('C6')
    elif (Value == "3"):
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/pig_sound.mp3") #Pig
        pygame.mixer.music.play()
        for i in range(row):
            for j in range(col):
                button[i][j].config(bg="#CBC3E3")#pig
        time.sleep(10)
        button[2][2].config(bg="black"), button[2][3].config(bg="black"), button[2][4].config(bg="black"), button[2][13].config(bg="black"), button[2][14].config(bg="black"), button[2][15].config(bg="black"), button[3][1].config(bg="black")
        button[3][5].config(bg="black"), button[3][6].config(bg="black"), button[3][7].config(bg="black"), button[3][8].config(bg="black"), button[3][9].config(bg="black"), button[3][10].config(bg="black"), button[3][11].config(bg="black")
        button[3][12].config(bg="black"), button[3][16].config(bg="black"), button[4][1].config(bg="black"), button[4][16].config(bg="black"), button[5][2].config(bg="black"), button[5][3].config(bg="black"), button[5][14].config(bg="black")
        button[5][15].config(bg="black"), button[6][2].config(bg="black"), button[6][4].config(bg="black"), button[6][5].config(bg="black"), button[6][12].config(bg="black"), button[6][13].config(bg="black"), button[6][15].config(bg="black")
        button[7][1].config(bg="black"), button[7][4].config(bg="black"), button[7][5].config(bg="black"), button[7][12].config(bg="black"), button[7][13].config(bg="black"), button[7][16].config(bg="black"),  button[8][1].config(bg="black")
        button[8][6].config(bg="black"), button[8][7].config(bg="black"), button[8][8].config(bg="black"), button[8][9].config(bg="black"), button[8][10].config(bg="black"), button[8][11].config(bg="black"), button[9][1].config(bg="black")
        button[9][5].config(bg="black"), button[9][12].config(bg="black"), button[9][16].config(bg="black"), button[10][1].config(bg="black"), button[10][5].config(bg="black"), button[10][7].config(bg="black"), button[10][10].config(bg="black")
        button[10][12].config(bg="black"), button[10][16].config(bg="black"), button[11][1].config(bg="black"), button[11][5].config(bg="black"), button[11][12].config(bg="black"), button[11][16].config(bg="black"), button[12][2].config(bg="black")
        button[12][6].config(bg="black"), button[12][7].config(bg="black"), button[12][8].config(bg="black"), button[12][9].config(bg="black"), button[12][10].config(bg="black"), button[12][11].config(bg="black"), button[12][15].config(bg="black")
        button[13][2].config(bg="black"), button[13][15].config(bg="black"), button[14][3].config(bg="black"), button[14][5].config(bg="black"), button[14][12].config(bg="black"), button[14][14].config(bg="black"), button[15][3].config(bg="black")
        button[13][2].config(bg="black"), button[15][6].config(bg="black"), button[15][7].config(bg="black"), button[15][8].config(bg="black"), button[15][9].config(bg="black"), button[15][10].config(bg="black"), button[15][11].config(bg="black")
        button[15][14].config(bg="black"), button[16][3].config(bg="black"), button[16][6].config(bg="black"), button[16][11].config(bg="black"), button[16][14].config(bg="black"), button[17][3].config(bg="black"), button[17][4].config(bg="black")
        button[17][5].config(bg="black"), button[17][6].config(bg="black"), button[17][11].config(bg="black"), button[17][12].config(bg="black"), button[17][13].config(bg="black"), button[17][14].config(bg="black"), button[8][16].config(bg="black")
        button[3][2].config(bg="pink"), button[3][3].config(bg="pink"), button[3][4].config(bg="pink"), button[3][13].config(bg="pink"), button[3][14].config(bg="pink"), button[3][15].config(bg="pink"), button[4][2].config(bg="pink")
        button[4][3].config(bg="pink"), button[4][4].config(bg="pink"), button[4][5].config(bg="pink"), button[4][6].config(bg="pink"), button[4][7].config(bg="pink"), button[4][8].config(bg="pink"), button[4][9].config(bg="pink")
        button[4][10].config(bg="pink"), button[4][11].config(bg="pink"), button[4][12].config(bg="pink"), button[4][13].config(bg="pink"), button[4][14].config(bg="pink"), button[4][15].config(bg="pink"), button[5][4].config(bg="pink")
        button[5][5].config(bg="pink"), button[5][6].config(bg="pink"), button[5][7].config(bg="pink"), button[5][8].config(bg="pink"), button[5][9].config(bg="pink"), button[5][10].config(bg="pink"), button[5][11].config(bg="pink"),
        button[5][12].config(bg="pink"), button[5][13].config(bg="pink"), button[6][3].config(bg="pink"), button[6][6].config(bg="pink"), button[6][7].config(bg="pink"), button[6][8].config(bg="pink"), button[6][9].config(bg="pink")
        button[6][10].config(bg="pink"), button[6][11].config(bg="pink"), button[6][14].config(bg="pink"), button[7][2].config(bg="pink"), button[7][3].config(bg="pink"), button[7][6].config(bg="pink"), button[7][7].config(bg="pink")
        button[7][8].config(bg="pink"), button[7][9].config(bg="pink"), button[7][10].config(bg="pink"), button[7][11].config(bg="pink"), button[7][14].config(bg="pink"), button[7][15].config(bg="pink"), button[8][2].config(bg="pink")
        button[8][3].config(bg="pink"), button[8][4].config(bg="pink"), button[8][5].config(bg="pink"), button[8][12].config(bg="pink"), button[8][13].config(bg="pink"), button[8][14].config(bg="pink"), button[8][15].config(bg="pink")
        button[9][2].config(bg="pink"), button[9][3].config(bg="pink"), button[9][4].config(bg="pink"), button[9][6].config(bg="pink"), button[9][7].config(bg="pink"), button[9][8].config(bg="pink"), button[9][9].config(bg="pink")
        button[9][10].config(bg="pink"), button[9][11].config(bg="pink"), button[10][2].config(bg="pink"), button[10][3].config(bg="pink"), button[10][4].config(bg="pink"), button[10][6].config(bg="pink"), button[10][8].config(bg="pink")
        button[10][9].config(bg="pink"), button[10][11].config(bg="pink"), button[10][13].config(bg="pink"), button[10][14].config(bg="pink"), button[10][15].config(bg="pink"), button[11][2].config(bg="pink")
        button[11][3].config(bg="pink"), button[11][4].config(bg="pink"), button[11][6].config(bg="pink"), button[11][7].config(bg="pink"), button[11][8].config(bg="pink"), button[11][9].config(bg="pink"), button[11][10].config(bg="pink")
        button[11][11].config(bg="pink"), button[11][13].config(bg="pink"), button[11][14].config(bg="pink"), button[11][15].config(bg="pink"), button[12][3].config(bg="pink"), button[12][4].config(bg="pink"), button[12][5].config(bg="pink")
        button[12][12].config(bg="pink"), button[12][13].config(bg="pink"), button[12][14].config(bg="pink"), button[13][3].config(bg="pink"), button[13][4].config(bg="pink"), button[13][5].config(bg="pink"), button[13][6].config(bg="pink")
        button[13][7].config(bg="pink"), button[13][8].config(bg="pink"), button[13][9].config(bg="pink"), button[13][10].config(bg="pink"), button[13][11].config(bg="pink"), button[13][12].config(bg="pink"), button[13][13].config(bg="pink")
        button[13][14].config(bg="pink"), button[14][4].config(bg="pink"), button[14][6].config(bg="pink"), button[14][7].config(bg="pink"), button[14][8].config(bg="pink"), button[14][9].config(bg="pink"), button[14][10].config(bg="pink")
        button[14][11].config(bg="pink"), button[14][13].config(bg="pink"), button[15][4].config(bg="pink"), button[15][5].config(bg="pink"), button[15][12].config(bg="pink"), button[15][13].config(bg="pink"), button[16][4].config(bg="pink")
        button[16][5].config(bg="pink"), button[16][12].config(bg="pink"), button[16][13].config(bg="pink"), button[9][13].config(bg="pink"), button[9][14].config(bg="pink"), button[9][15].config(bg="pink")
        toggle = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        BPM_slider.set(180)
        profileClicked.set('pluck')
        keyClicked.set('C3')
    elif (Value == "4"):
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/panda_sound.mp3") #Panda
        pygame.mixer.music.play()
        for i in range(row):
            for j in range(col):
                button[i][j].config(bg="#CBC3E3")
        time.sleep(16)
        button[4][3].config(bg="black"), button[4][4].config(bg="black"), button[4][13].config(bg="black"), button[4][14].config(bg="black"), button[5][1].config(bg="black"), button[5][2].config(bg="black"), button[5][3].config(bg="black")
        button[5][4].config(bg="black"), button[5][5].config(bg="black"), button[5][7].config(bg="black"), button[5][8].config(bg="black"), button[5][9].config(bg="black"), button[5][10].config(bg="black"), button[5][12].config(bg="black")
        button[5][13].config(bg="black"), button[5][14].config(bg="black"), button[5][15].config(bg="black"), button[5][16].config(bg="black"), button[6][1].config(bg="black"), button[6][2].config(bg="black"), button[6][3].config(bg="black")
        button[6][4].config(bg="black"), button[6][5].config(bg="black"), button[6][6].config(bg="black"), button[6][11].config(bg="black"), button[6][12].config(bg="black"), button[6][13].config(bg="black"), button[6][14].config(bg="black")
        button[6][15].config(bg="black"), button[6][16].config(bg="black"), button[7][1].config(bg="black"), button[7][2].config(bg="black"), button[7][3].config(bg="black"), button[7][4].config(bg="black"), button[7][13].config(bg="black")
        button[7][14].config(bg="black"), button[7][15].config(bg="black"), button[7][16].config(bg="black"), button[8][1].config(bg="black"), button[8][2].config(bg="black"), button[8][3].config(bg="black"), button[8][14].config(bg="black")
        button[8][15].config(bg="black"), button[8][16].config(bg="black"), button[9][2].config(bg="black"), button[9][15].config(bg="black"), button[10][2].config(bg="black"), button[10][5].config(bg="black"), button[10][6].config(bg="black")
        button[10][11].config(bg="black"), button[10][12].config(bg="black"), button[10][15].config(bg="black"), button[11][1].config(bg="black"), button[11][4].config(bg="black"), button[11][5].config(bg="black"), button[11][6].config(bg="black")
        button[11][11].config(bg="black"),button[11][12].config(bg="black"), button[11][13].config(bg="black"), button[11][16].config(bg="black"), button[12][1].config(bg="black"), button[12][4].config(bg="black"), button[12][5].config(bg="black")
        button[12][6].config(bg="black"), button[12][11].config(bg="black"), button[12][13].config(bg="black"), button[12][16].config(bg="black"), button[13][1].config(bg="black"), button[13][4].config(bg="black"), button[13][6].config(bg="black")
        button[13][11].config(bg="black"), button[13][13].config(bg="black"), button[13][16].config(bg="black"), button[14][1].config(bg="black"), button[14][4].config(bg="black"), button[14][5].config(bg="black"), button[14][6].config(bg="black")
        button[14][8].config(bg="black"), button[14][9].config(bg="black"), button[14][11].config(bg="black"),button[14][12].config(bg="black"), button[14][13].config(bg="black"), button[14][16].config(bg="black"), button[15][2].config(bg="black")
        button[15][7].config(bg="black"), button[15][10].config(bg="black"), button[15][15].config(bg="black"), button[16][3].config(bg="black"), button[16][4].config(bg="black"), button[16][13].config(bg="black"), button[16][14].config(bg="black")
        button[17][5].config(bg="black"), button[17][6].config(bg="black"), button[17][7].config(bg="black"), button[17][8].config(bg="black"), button[17][9].config(bg="black"), button[17][10].config(bg="black"), button[17][11].config(bg="black")
        button[17][12].config(bg="black")
        toggle = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
                  [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #PANDA
        BPM_slider.set(180)
        profileClicked.set('sawtooth')
        keyClicked.set('C4')
    else:
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/dog_sound.mp3") #Dog
        pygame.mixer.music.play()
        for i in range(row):
            for j in range(col):
                button[i][j].config(bg="#CBC3E3")#dog
        time.sleep(5)
        button[5][3].config(bg="black"),  button[5][4].config(bg="black"),  button[5][6].config(bg="black"),  button[5][7].config(bg="black"),  button[5][8].config(bg="black"),  button[5][9].config(bg="black"),  button[5][10].config(bg="black")
        button[5][12].config(bg="black"), button[5][13].config(bg="black"), button[6][2].config(bg="black"), button[6][5].config(bg="black"), button[6][11].config(bg="black"), button[6][14].config(bg="black"), button[7][1].config(bg="black")
        button[7][15].config(bg="black"), button[8][1].config(bg="black"), button[8][4].config(bg="black"), button[8][12].config(bg="black"), button[8][15].config(bg="black"), button[9][1].config(bg="black"), button[9][3].config(bg="black")
        button[9][4].config(bg="black"), button[9][6].config(bg="black"), button[9][10].config(bg="black"), button[9][12].config(bg="black"), button[9][13].config(bg="black"), button[9][15].config(bg="black"), button[10][1].config(bg="black")
        button[10][2].config(bg="black"), button[10][4].config(bg="black"), button[10][6].config(bg="black"), button[10][10].config(bg="black"), button[10][12].config(bg="black"), button[10][14].config(bg="black"), button[10][15].config(bg="black")
        button[11][4].config(bg="black"), button[11][12].config(bg="black"), button[12][4].config(bg="black"), button[12][7].config(bg="black"), button[12][8].config(bg="black"), button[12][9].config(bg="black"), button[12][12].config(bg="black")
        button[13][4].config(bg="black"), button[13][8].config(bg="black"), button[13][12].config(bg="black"), button[14][5].config(bg="black"), button[14][6].config(bg="black"), button[14][7].config(bg="black"), button[14][8].config(bg="black")
        button[14][9].config(bg="black"), button[14][10].config(bg="black"), button[14][11].config(bg="black"), button[6][3].config(bg="brown"), button[6][4].config(bg="brown"), button[7][2].config(bg="brown"), button[7][3].config(bg="brown")
        button[7][4].config(bg="brown"), button[7][5].config(bg="brown"), button[11][9].config(bg="brown"), button[11][10].config(bg="brown"), button[8][9].config(bg="brown"), button[9][9].config(bg="brown"), button[10][9].config(bg="brown")
        button[8][10].config(bg="brown"), button[8][11].config(bg="brown"), button[9][11].config(bg="brown"), button[10][11].config(bg="brown")
        toggle = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        BPM_slider.set(180)
        profileClicked.set('trapezium')
        keyClicked.set('C5')

def translating(Value):
    translator = Translator(from_choiceg = choice1.get(),
                            to_lang = choice2.get())
    translation = translator.translate(var.get())
    var1.set(translation)
    print(translation)
    if (Value == 'Chinese'):
        language = 'zh'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
    elif (Value == 'Malay'):
        language = 'id'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
    elif (Value == 'Korean'):
        language = 'ko'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
    elif (Value == 'Japanese'):
        language = 'ja'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
    elif (Value == 'Tamil'):
        language = 'ta'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
    elif (Value == 'French'):
        language = 'fr'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
    elif (Value == 'Spanish'):
        language = 'es-es'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
    elif (Value == 'Vietnamese'):
        language = 'vi'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
    elif (Value == 'Thai'):
        language = 'th'
        speech = gTTS(text = translation, lang = language, slow = False)
        speech.save("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        time.sleep(1)
        pygame.mixer.music.load("/home/pi/sorpiart-teamEfyp/Sound/mp3/translated_text.mp3")
        pygame.mixer.music.play()
        
                
bg = PIL.Image.open("/home/pi/sorpiart-teamEfyp/icon/proj_bg1.png")
bg = bg.resize((1919,1065))
img = ImageTk.PhotoImage(bg)
label = Label(tab1, image = img)
label2 = Label(tab2, image = img)
label3 = Label(tab3, image = img)
label4 = Label(tab4, image = img)
label.place(x = 0, y = 0)
label2.place(x = 0, y = 0)
label3.place(x = 0, y = 0)
label4.place(x = 0, y =0)
    
toggle = [i for i in range(row)]
for i in range(row):
    toggle[i] = [j for j in range(col)]
for i in range(row):
    for j in range(col):
        toggle[i][j] = 0
        
unselected = [i for i in range(row)]
for i in range(row):
    unselected[i] = [j for j in range(col)]
for i in range(row):
    for j in range(col):
        unselected[i][j] = 0


button = [i for i in range(row)] 
for i in range(row):
    button[i] = [j for j in range(col)]
for i in range(row):
    for j in range(col):
        button[i][j] = tk.Button(tab1, text = "{}".format(notes[j]), padx = 8, pady = 12, height=1, width=4, bg = "#CBC3E3", font = ("Flavors 10"), command=lambda idx = i, jdx = j: click(idx, jdx))
        button[i][j].grid(row = i, column = j, sticky = "ew")
        
#Activity: Guess the Animal
animal_label = tk.Label(tab1, text="GUESS THE ANIMAL", font = ("Flavors 19"), bg='#D6ECE2')
animal_label.grid(row = 6, column = 21)
animal = ["1", "2", "3", "4", "5"]
animalClicked = StringVar(main)
animalClicked.set(animal[0])
animalDrop = tk.OptionMenu(tab1, animalClicked, *animal, command = func)

#dropdown for Sound Profile
profile_label = tk.Label(tab1, text = "Profile", font = ("Flavors 19"), bg='#D6ECE2')
profile = ["sine", "square", "triangle", "pluck","sawtooth", "trapezium"]
profileClicked = StringVar(main)
profileClicked.set(profile[0])
profileDrop = tk.OptionMenu(tab1, profileClicked, *profile)

#dropdown for Key
key_label = tk.Label(tab1, text = "Key", font = ("Flavors 19"), bg='#D6ECE2')
key = ["C1", "C2", "C3", "C4", "C5", "C6"]
keyClicked = StringVar(main)
keyClicked.set(key[0])
keyDrop = tk.OptionMenu(tab1, keyClicked, *key)

#slider for BPM
BPM_slider_label = tk.Label(tab1, text = "BPM", font = ("Flavors 19"), bg='#D6ECE2')
BPM_slider = tk.Scale(tab1, from_ = 60, to = 180, orient = HORIZONTAL, bg = "light yellow")

#reset button
reset_button = tk.Button(tab1, text = "reset", command = reset, bg = "blue", fg = "white", font = ("Flavors 19"))

#play button
play_button = tk.Button(tab1 ,text = "play sound", command = play, bg = "blue", fg = "white", font = ("Flavors 19"))

#instructions button for grid
instruction_button = tk.Button(tab1, text = "Instructions", command = pix2music_instructions, font = ("Flavors 19"), bg = "blue", fg = "white")


##recording program
recording_program_label = tk.Label(tab2, text = "Voice to Picture Recorder", font = ("Flavors 35"), bg='#D6ECE2')
recording_program_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)
recording_btn = tk.Button(tab2, text="Start Recording", command = Recording, font = ("Flavors 19"), bg='#D6ECE2')
recording_btn.place(relx=0.5, rely=0.3, anchor = CENTER)


##beatmaker program
drumIcon = ImageTk.PhotoImage(PIL.Image.open("/home/pi/sorpiart-teamEfyp/icon/drums.png").resize((60, 60), PIL.Image.ANTIALIAS))
pianoIcon = ImageTk.PhotoImage(PIL.Image.open("/home/pi/sorpiart-teamEfyp/icon/piano.png").resize((60,60), PIL.Image.ANTIALIAS))

beatmaker_title = tk.Label(tab3, text="Sound Launchpad with Buttons", font = ("Flavors 50"), bg='#D6ECE2')
beatmaker_title.place(relx=0.5, rely=0.2, anchor = CENTER)

piano_label = tk.Label(tab3, text="PIANO", font = ("Flavors 25"), bg='#D6ECE2')
piano_label.place(relx = 0.45, rely = 0.29, anchor = CENTER) 
piano_btn = tk.Button(tab3, image=pianoIcon, command = beatmaker_piano, bg='#D6ECE2')
piano_btn.place(relx = 0.45, rely = 0.35, anchor = CENTER)

drum_label = tk.Label(tab3, text="DRUMS", font = ("Flavors 25"), bg='#F2F9F7')
drum_label.place(relx = 0.55, rely = 0.29, anchor = CENTER)
drums_btn = tk.Button(tab3, image=drumIcon, command = beatmaker_drums)
drums_btn.place(relx = 0.55, rely = 0.35, anchor = CENTER)

#beatmaker instructions button
beatmaker_instructions = tk.Button(tab3, text="Instructions", command = beatmaker_instructions, font = ("Flavors 19"), bg='#D6ECE2')
beatmaker_instructions.place(relx = 0.5, rely = 0.45, anchor = CENTER)


##Translator Program
choices = ['Chinese', 'Malay', 'Korean', 'Japanese','Tamil', 'French', 'Spanish', 'Vietnamese', 'Thai']
translator_program_title = Label(tab4, text="Translate from English to other languages", font = ("Flavors 30"), bg='#D6ECE2')
translator_program_title.place(relx = 0.5, rely = 0.3, anchor = CENTER)

#input
choice1 = StringVar(tab4)
choice1.set('English')
input_choice = Label(tab4, font = ("Flavors 19"), bg='#D6ECE2')
input_choice.place(relx = 0.5, rely = 0.3, anchor = CENTER)
var = StringVar()
input_textbox = Entry(tab4, textvariable = var, width = 50)
input_textbox.place(relx = 0.5, rely = 0.35, anchor = CENTER)

#output
choice2 = StringVar(tab4)
choice2.set('')
output_choice = Label(tab4, text = "CHOOSE LANGUGE TO TRANSLATE TO", font = ("Flavors 30"), bg='#D6ECE2')
output_choice.place(relx = 0.5, rely = 0.45, anchor = CENTER)
translated_languages = OptionMenu(tab4, choice2, *choices, command = translating)
translated_languages.place(relx = 0.5, rely = 0.5, anchor = CENTER)
var1 = StringVar()
output_textbox = Entry(tab4, textvariable = var1, width = 50)
output_textbox.place(relx = 0.5, rely = 0.55, anchor = CENTER)


#arrange buttons
key_label.grid(row = 0, column = 19)
keyDrop.grid(row = 0, column = 21, sticky = "ew")
BPM_slider_label.grid(row = 1, column = 19)
BPM_slider.grid(row = 1, column = 21, sticky = "ew")
profile_label.grid(row = 2, column = 19)
profileDrop.grid(row = 2, column = 21, sticky = "ew")
play_button.grid(row = 3, column = 21, sticky = "ew")
reset_button.grid(row = 4, column = 21, sticky = "ew")
instruction_button.grid(row = 5, column = 21, sticky = "ew")
animalDrop.grid(row = 7, column = 21)

main.mainloop()
