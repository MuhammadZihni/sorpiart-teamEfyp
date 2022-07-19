import tkinter as tk
from gpiozero import *
import pygame
import random
from PIL import Image, ImageTk

# main = tk.Tk()

# def beat_maker():
#     row,  col = 2, 4
pygame.mixer.init()

# colors = ['red', 'green', 'blue', 'yellow', 'orange', 'magenta', 'cyan']
# 
# drumIcon = ImageTk.PhotoImage(Image.open("/home/pi/project/pictures/drums.png").resize((60, 60), Image.ANTIALIAS))
# pianoIcon = ImageTk.PhotoImage(Image.open("/home/pi/project/pictures/piano.png").resize((60,60), Image.ANTIALIAS))

btn_kick = Button(25)
btn_snare = Button(8)
btn_hihat = Button(7)
btn_midtom = Button(0)
btn_hightom = Button(1)
btn_floortom = Button(5)
btn_ridecymbal = Button(6)
btn_crashcymbal = Button(12)


kick_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/kick.wav')
hihat_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/hi-hat.wav')
snare_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/snare.wav')
midtom_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/mid-tom.wav')
hightom_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/high-tom.wav')
floortom_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/floor-tom.wav')
ridecymbal_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/ride_cymbal.wav')
crashcymbal_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/crash_cymbal.wav')
# cowbell_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/cowbell.wav')
# triangle_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/triangle.wav')
# gong_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/gong.wav')
# castanets_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/castanets.wav')
do_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/do.wav')
re_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/re.wav')
mi_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/mi.wav')
fa_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/fa.wav')
sol_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/sol.wav')
la_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/la.wav')
si_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/si.wav')
do1_sound = pygame.mixer.Sound('/home/pi/project/Sound/wav/do1.wav')

is_on = True


# def play(i, j):
#     if button[i][j] == button[0][0]:
#         kick_sound.play()
#     elif button[i][j] == button[0][1]:
#         hihat_sound.play()
#     elif button[i][j] == button[0][2]:
#         snare_sound.play()
#     elif button[i][j] == button[0][3]:
#         midtom_sound.play()
#     elif button[i][j] == button[1][0]:
#         hightom_sound.play()
#     elif button[i][j] == button[1][1]:
#         floortom_sound.play()
#     elif button[i][j] == button[1][2]:
#         ridecymbal_sound.play()
#     elif button[i][j] == button[1][3]:
#         crashcymbal_sound.play()
        
def piano():
    btn_kick.when_pressed = do_sound.play
    btn_hihat.when_pressed = re_sound.play
    btn_snare.when_pressed = mi_sound.play
    btn_floortom.when_pressed = fa_sound.play
    btn_midtom.when_pressed = sol_sound.play
    btn_hightom.when_pressed = la_sound.play
    btn_ridecymbal.when_pressed = si_sound.play
    btn_crashcymbal.when_pressed = do1_sound.play

def drum():
    btn_kick.when_pressed = kick_sound.play
    btn_hihat.when_pressed = hihat_sound.play
    btn_snare.when_pressed = snare_sound.play
    btn_midtom.when_pressed = midtom_sound.play
    btn_hightom.when_pressed = hightom_sound.play
    btn_floortom.when_pressed = floortom_sound.play
    btn_ridecymbal.when_pressed = ridecymbal_sound.play
    btn_crashcymbal.when_pressed = crashcymbal_sound.play
    
                
    
        
# button = [i for i in range(row)]
# for i in range(row):
#     button[i] = [j for j in range(col)]
# for i in range(row):
#     for j in range(col):
#         randomColors = random.choice(colors)
#         button[i][j] = tk.Button(main, bg=randomColors, width=5, height=3, command=lambda idx=i, jdx=j: play(idx, jdx)) 
#         button[i][j].grid(row=i, column=j)
# instructionsLabel = tk.Label(main, text="Sound Launchpad with Buttons")
# instructionsLabel.grid(row=1, column=2)
# # 
# drum_button = tk.Button(main, image=drumIcon, borderwidth=0, command=drum)
# drum_button.grid(row=3, column=2)
# 
# piano_button = tk.Button(main, image=pianoIcon, borderwidth=0, command=piano)
# piano_button.grid(row=4, column=2)


btn_kick.when_pressed = kick_sound.play
btn_hihat.when_pressed = hihat_sound.play
btn_snare.when_pressed = snare_sound.play
btn_midtom.when_pressed = midtom_sound.play
btn_hightom.when_pressed = hightom_sound.play
btn_floortom.when_pressed = floortom_sound.play
btn_ridecymbal.when_pressed = ridecymbal_sound.play
btn_crashcymbal.when_pressed = crashcymbal_sound.play
# btn_cowbell.when_pressed = cowbell_sound.play
# btn_triangle.when_pressed = triangle_sound.play
# btn_gong.when_pressed = gong_sound.play
# btn_castanets.when_pressed = castanets_sound.play

        