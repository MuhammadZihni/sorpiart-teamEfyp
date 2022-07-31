# sorpiart
Raspberry Pi project on "Painting with Sound"

## To run Tkinter GUI on boot
In order to run your tkinter gui script (**e.g. main.py**) everytime the **Raspberry Pi** boots up, we can utilise on **autostart**. 

### Configuration (autostart)
1. open terminal
2. change directory to **.config**
2.1 `cd .config/`22
3. Create an **autostart** folder
3.1 `mkdir autostart`
4. copy **tkinterautostart.desktop** into the folder
4.1 `cp ~/sorpiart/tkinterautostart.desktop ~/.config/autostart/`
5. edit **tkinterautostart.desktop** 
5.1 `nano ~/.config/autostart/tkinterautostart.desktop`

## To install sox library (pix2music)
In order for **pix2music.py** to work, the **Raspberry Pi** will require the **Sound Exchange (sox)** library to be installed.

To install **sox**
1. open terminal
2. `sudo apt install sox`

## Setup
To start off, we will need to install a list of modules on our Raspberry Pi. We will install all these modules using the terminal.
1. **sox library**. <br />
    - `sudo apt install sox`
    


## To use Twitter Bot to upload images and captions automatically
In order for the Twitter Bot to work, here are a few things that you need:
    - twython module
    - Twitter developer account
    - Twitter application

Installation of modules/libraries

To install the **twython** module
    1. Open terminal
    2. `sudo pip3 install twython (python3) / sudo pip install twython (python2)` 

To install the **pygame** module
    1. Open terminal
    2. Enter `sudo apt-get install python-pygame`
    3. In python code, `import pygame`

To install the **pyaudio** module
    1. Open terminal
    2. Enter `sudo pip install pyaudio`
    3. In python code, `import pyaudio`

To install the **numpy** module
    1. Open terminal 
    2. Enter `sudo apt install python3-numpy`
    3. run `sudo pip3 install numpy`

To install the **matplotlib** module
    1. Open terminal 
    2. Run `sudo apt install python3-matplkotlib python3-tk` and
    `sudo pip3 install matplotlib pytk`

To install the **PIL a.k.a pillow**
    1. Open terminal 
    2. Enter `sudo pip install pillow`

To install the **scipy**
    1. Open terminal
    2. Enter `sudo apt-get install python3-scipy`


Apply for a Twitter developer account
1. Create a Twitter account (if you don't already have one) at [twitter.com](https://twitter.com)
2. Apply for a Twitter developer account at [developer.twitter.com](https://developer.twitter.com)


