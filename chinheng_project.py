from tkinter import *
import tkinter as tk
from tkinter import ttk
from pix2music import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt
from beatmaker import *


main = Tk()
main.geometry("2100x1100")
tabControl = ttk.Notebook(main)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Tab 1")
tabControl.add(tab2, text="Tab 2")
tabControl.add(tab3, text="Beatmaker")
tabControl.pack(expand=1, fill="both")  #expand = expand to fill any space not otherwise used. fill= fil space on x and y axis

row, col = 15, 15
notes=["do","re","mi","fa","so","la","ti","do","re","mi","fa","so","la","ti","do"]

def click(i, j):
    global toggle
    if toggle[i][j] == 0: 
        toggle[i][j] = 1
        button[i][j].config(bg="light blue")
    else:
        toggle[i][j] = 0
        button[i][j].config(bg="light green") 
    
    
def reset():
    global i,j
    profileClicked.set(profile[0])
    keyClicked.set(key[0])
    BPM_slider.set(60)
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="light green")
            
def play():
    global toggle, unselected
    print(toggle)
    if toggle==unselected:
        messagebox.showwarning("warning","Please select a note")
    else:
        pix2music(profileClicked.get(), BPM_slider.get(), keyClicked.get(), toggle)
        print("Profile is {}".format(profileClicked.get()))
        print("Key is {}".format(keyClicked.get()))
        print("BPM is {}".format(BPM_slider.get()))
        
        
def SAW():
    print("Profile is saw")
    
def PLUCK():
    print("Profile is pluck")

def TRIANGLE():
    print("Profile is triangle")
    
def Recording():
    subprocess.Popen(["python3", "/home/pi/project/EGL314_Project_TeamC/recording.py"])
    
def beatmaker_piano():
    piano()
    piano_label.config(fg="blue")
    drum_label.config(fg="black")
    print("piano mode activated")
    
def beatmaker_drums():
    drum()
    drum_label.config(fg="blue")
    piano_label.config(fg="black")

bg = Image.open("/home/pi/project/pictures/proj_bg1")
bg = bg.resize((1920,1015))
img = ImageTk.PhotoImage(bg)
label = Label(tab1, image = img)
label.place(x = 0, y = 0)
    
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
        button[i][j] = tk.Button(tab1, text = "{}".format(notes[j]), padx = 15, pady = 15, bg = "light green", command=lambda idx = i, jdx = j: click(idx, jdx))
        button[i][j].grid(row = i, column = j, sticky = "ew")

#dropdown for Sound Profile
profile = ["Sine", "Square", "Triangle", "pluck","sawtooth", "trapezium"]
profileClicked = StringVar(main)
profileClicked.set(profile[0])
profileDrop = tk.OptionMenu(tab1, profileClicked, *profile)

#button for saw profile
saw = PhotoImage(file = r"/home/pi/project/pictures/saw")
saw_button = tk.Button(tab1, image = saw, command = SAW)
saw_button.place(x=900,y=50)

#button for pluck profile
pluck = PhotoImage(file = r"/home/pi/project/pictures/pluck")
pluck_button = tk.Button(tab1, image = pluck, command = PLUCK)
pluck_button.place(x=1000,y=50)

#button for triangle profile
triangle = PhotoImage(file = r"/home/pi/project/pictures/triangle")
triangle_button = tk.Button(tab1, image = triangle, command = TRIANGLE)
triangle_button.place(x=1100,y=50)

#dropdown for Key
key = ["C1", "C2", "C3", "C4", "C5", "C6"]
keyClicked = StringVar(main)
keyClicked.set(key[0])
keyDrop = tk.OptionMenu(tab1, keyClicked, *key)

#slider for BPM
BPM_slider = tk.Scale(tab1, from_ = 60, to = 180, orient = HORIZONTAL, bg = "light yellow")

#reset button
reset_button = tk.Button(tab1, text = "reset", command = reset, bg = "blue", fg = "white", font = ("Flavors 16"))

#play button
play_button = tk.Button(tab1 ,text = "play sound", command=play, bg = "blue", fg = "white", font = ("Flavors 16"))


recording_btn = tk.Button(tab2, text="click here to open the recording program", command = Recording)
recording_btn.grid(row=1, column=1)

#beatmaker
drumIcon = ImageTk.PhotoImage(Image.open("/home/pi/project/pictures/drums.png").resize((60, 60), Image.ANTIALIAS))
pianoIcon = ImageTk.PhotoImage(Image.open("/home/pi/project/pictures/piano.png").resize((60,60), Image.ANTIALIAS))

instructionsLabel = tk.Label(tab3, text="Sound Launchpad with Buttons")
instructionsLabel.place(relx=0.5, rely=0.2, anchor = 'center')

piano_btn = tk.Button(tab3, image=pianoIcon, command = beatmaker_piano, anchor = 'center')
piano_btn.place(x=850, y=300)
piano_label = tk.Label(tab3, text="PIANO")
piano_label.place(x=858, y=260)

drums_btn = tk.Button(tab3, image=drumIcon, command = beatmaker_drums, anchor = 'center')
drums_btn.place(x=1000, y=300)
drum_label = tk.Label(tab3, text="DRUMS")
drum_label.place(x=1005, y=260)

#arrange buttons
keyDrop.grid(row = 1, column = 17, sticky = "ew")
BPM_slider.grid(row = 2, column = 17, sticky = "ew")
profileDrop.grid(row = 3, column = 17, sticky = "ew")
play_button.grid(row = 4, column = 17, sticky = "ew")
reset_button.grid(row = 5, column = 17, sticky = "ew")



main.mainloop()