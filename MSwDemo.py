#Demonstration of Toggle Switch 
#Using GPIO 31 as Input

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

MSw=29

# Set 29 for Input as Momentary Switch
# Make sure to tell RPi how you wired the switch!!
GPIO.setup(MSw,GPIO.IN,pull_up_down=GPIO.PUD_UP)

MSwNum=0
while True:
	if GPIO.input(MSw)==False:
		MSwNum=MSwNum+1
		print("Switch Pushed=",MSwNum)
		while GPIO.input(MSw)==False:
			#Wait for switc to finish bouncing! 
			time.sleep(.2)
