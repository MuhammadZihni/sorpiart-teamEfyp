from gpiozero import *                                                                                           
import pygame
import RPi.GPIO as GPIO

pygame.mixer.init()

btn_kick = Button(25)
btn_snare = Button(8)
btn_hihat = Button(7)
btn_midtom = Button(0)
btn_hightom = Button(1)
btn_floortom = Button(5)
btn_ridecymbal = Button(6)
btn_crashcymbal = Button(12)


kick_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/kick.wav')
hihat_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/hi-hat.wav')
snare_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/snare.wav')
midtom_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/mid-tom.wav')
hightom_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/high-tom.wav')
floortom_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/floor-tom.wav')
ridecymbal_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/ride-cymbal.wav')
crashcymbal_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/crash-cymbal.wav')

do_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/do.wav')
re_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/re.wav')
mi_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/mi.wav')
fa_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/fa.wav')
sol_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/sol.wav')
la_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/la.wav')
si_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/si.wav')
do1_sound = pygame.mixer.Sound('/home/pi/project/EGL314_Project_TeamC/Sound/wav/do1.wav')


is_on = True
   
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
    
    
# btn_kick.when_pressed = kick_sound.play
# btn_hihat.when_pressed = hihat_sound.play
# btn_snare.when_pressed = snare_sound.play
# btn_midtom.when_pressed = midtom_sound.play
# btn_hightom.when_pressed = hightom_sound.play
# btn_floortom.when_pressed = floortom_sound.play
# btn_ridecymbal.when_pressed = ridecymbal_sound.play
# btn_crashcymbal.when_pressed = crashcymbal_sound.play

        