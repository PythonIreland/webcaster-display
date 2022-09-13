# webcaster-display
The display node client for the webcaster project


This is intented to run on a raspberry pi

https://reelyactive.github.io/diy/pi-kiosk/

set kiosk mode


    # Install xserver utils with the command 
    sudo apt-get install --no-install-recommends xserver-xorg xinit x11-xserver-utils

Install Chromium and kiosk dependencies Part 3

From the same terminal
connected to the

Pi via SSH:

    # Install chromium-browser with the command 
    sudo apt-get install chromium-browser matchbox-window-manager xautomation unclutter


#!/bin/sh
export DISPLAY=:0 
xset -dpms     # disable DPMS (Energy Star) features.
xset s off     # disable screen saver
xset s noblank # don't blank the video device
matchbox-window-manager -use_titlebar no &
unclutter &    # hide X mouse cursor unless mouse activated
chromium-browser --display=:0 --kiosk --incognito --window-position=0,0 https://www.transportforireland.ie/live-travel-info-service-updates/live-departures/?departureId=8250DB000876&departureValue=Clonskeagh%2C%20Gledswood%20Drive%2C%20stop%20876


sudo apt-get install chromium-chromedriver


rotate screen
DISPLAY=:0 xrandr --output HDMI-1 --rotate right
DISPLAY=:0 xrandr --output HDMI-1 --rotate left
DISPLAY=:0 xrandr --output HDMI-1 --rotate inverted
reset
DISPLAY=:0 xrandr --output HDMI-1 --rotate normal


