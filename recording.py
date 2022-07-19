# Import the necessary modules.
import tkinter
import tkinter as tk
import tkinter.messagebox
import pyaudio
import wave
import os
import sys
import time
import subprocess


class RecAUD:

    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=1, rate=44100, py=pyaudio.PyAudio()):

        # Start Tkinter and set Title
        self.main = tkinter.Tk()
        self.collections = []
        self.main.geometry('500x300')
        self.main.title('Record')
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

        # Set Frames
        self.buttons = tkinter.Frame(self.main, padx=120, pady=20)

        # Pack Frame
        self.buttons.pack(fill=tk.BOTH)


        # Start and Stop buttons
        self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='Start Recording', command=lambda: self.start_record())
        self.strt_rec.grid(row=0, column=0, padx=50, pady=5)
        self.stop_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='Stop Recording', command=lambda: self.stop())
        self.stop_rec.grid(row=1, column=0, columnspan=1, padx=50, pady=5)
        
        self.recording_label = tkinter.Label(self.buttons, padx=10, pady=5, text="RECORDING")
        self.recording_label.grid(row=2, column=0, padx=50, pady=5, columnspan=1)
        
        self.processing_label = tkinter.Label(self.buttons, padx=10, pady=5, text="PROCESSING")
        self.processing_label.grid(row=3, column=0, padx=50, pady=5, columnspan=1)

        tkinter.mainloop()

    def start_record(self):
        self.recording_label.config(fg="red")
        self.processing_label.config(fg="black")
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            print("* recording")
            self.main.update()

        stream.close()
        
        wf = wave.open('test.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self):
        self.processing_label.config(fg="red")
        self.recording_label.config(fg="black")
        self.st = 0
        print("Recording Stopped")
        time.sleep(1)
        subprocess.Popen(["python3", "/home/pi/project/EGL314_Project_TeamC/displayingSpectrogram.py"])
        
        
    
# Create an object of the ProgramGUI class to begin the program.
guiAUD = RecAUD()