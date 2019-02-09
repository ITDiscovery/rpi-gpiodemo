#Demonstration of Toggle Switch 
#Using GPIO 31 as Input

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TSw=31
GreenLED=11
BlueLED=13

# Set 7 for Output as LED for Red
GPIO.setup(TSw,GPIO.IN,pull_up_down=GPIO.PUD_UP)

TSwState=True
while True:
   if GPIO.input(TSw) <> TSwState:
	TSwState=GPIO.input(TSw)
        if TSwState:
            print("Switch is Off")
	else:
	    print("Switch is On")

