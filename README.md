# sorpiart
Raspberry Pi project on "Painting with Sound"

## To run Tkinter GUI on boot
In order to run your tkinter gui script (**e.g. main.py**) everytime the **Raspberry Pi** boots up, we can utilise on **autostart**. 

### Configuration (autostart)
1. open terminal
2. change directory to **.config**
2.1 `cd .config/`
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

## To use Twitter Bot to upload images and captions automatically
In order for the Twitter Bot to work, here are a few things that you need:
    - twython module
    - Twitter developer account
    - Twitter application


To install the **twython** module
1. Open terminal
2. `sudo pip3 install twython (python3) / sudo pip install twython (python2)` 

Apply for a Twitter developer account
1. Create a Twitter account (if you don't already have one) at [twitter.com](https://twitter.com)
2. Apply for a Twitter developer account at [developer.twitter.com](https://developer.twitter.com)