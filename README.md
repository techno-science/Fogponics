# Description

This repository contains the code for the Fogponics project for the Canada Agriculture and Food Museum.

Using a Raspberry Pi 3 and a few other parts (listed below) this code will operate the system. This is "proof of concept" code and currently the pond fogger is not controlled by the Humidity Sensor. When to turn it on and off will change depending on your build, so we will leave it up to you to add this feature.

# Installation and setup

## Required Python Libraries

See these pages for how to install these libraries and for documentation.

* pi-sht1x
    * <https://github.com/drohm/pi-sht1x>
* Tornado
    * <http://www.tornadoweb.org/en/stable/>
* RPI-GPIO
    * <https://pypi.python.org/pypi/RPi.GPIO>
* websocket-client
	* <https://pypi.python.org/pypi/websocket-client/0.37.0>
	

## Running the system

The *fogponics.sh* shell script will run the system from the command-line. It can also be run from rc.local.

## Running the Browser

This is taken from [this tutorial](https://github.com/elalemanyo/raspberry-pi-kiosk-screen). See it for instructions for more browsers.

1. Install the Epiphany Browser, X11 server utilities, xautomation (for automating keystrokes) and unclutter (hides the cursor)
	```
	sudo apt-get install epiphany-browser x11-xserver-utils xautomation unclutter
	```

2. Make sure that the fullscreen.sh script is ready to run. Change it's file mode to:
	```
	sudo chmod 755 /home/pi/fullscreen.sh
	```

6. Add these lines to the autostart file for LXDE.
	```
	sudo nano ~/.config/lxsession/LXDE-pi/autostart
	```

	The autostart files needs to look like this (don't forget to change the path to the fullscreen.sh script):
	```
	@xset s off
	@xset -dpms
	@xset s noblank
	@[INSERT CORRECT PATH TO SCRIPT]/fullscreen.sh
	```

# How it Works (the quick version)

This system uses the Tornado python framework to read and display information from sensors to a web page using the WebSocket protocol

The *handlers* folder contains the python scripts that read incoming sensors/gpio data and pushes the information over the WebSocket.

The *template* and the *static* folders under server hold the web site that displays the data.

# Parts List

* Raspberry Pi 3
    * <http://www.newark.com/raspberrypi-boards#mk-pi-3-model-b>
* Soil Temperature/Moisture Sensor - SHT10
    * <https://www.adafruit.com/product/1298>
* Powerswitch tail 2
    * <https://www.adafruit.com/products/268>
* Mister
    * <http://www.mistmachine.ca/index.html#link2>

# Connection up the parts

Use the *Fogponics.fzz* in the docs folder for a diagram and schematic of the circuit. You can download the program [Fritzing](http://fritzing.org/home/) to view the drawing.
