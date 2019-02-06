#Demonstration of 3 Color LED
#Using GPIO 7 as Red, 11 as Green, 13 as Blue

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

RedLED=7
GreenLED=11
BlueLED=13

# Set 7 for Output as LED for Red
GPIO.setup(RedLED,GPIO.OUT)
# Set 11 for Output as LED for Green
GPIO.setup(GreenLED,GPIO.OUT)
# Set 13 for Output as LED for Blue
GPIO.setup(BlueLED,GPIO.OUT)

# Setup can open several ports at once:
# GPIO.setup([RedLED,GreenLED,BlueLED],GPIO.OUT)
# or even faster:
# LEDs=[7,11,13]
# GPIO.setup(LEDs,GPIO.OUT)

while True:
	GPIO.output(BlueLED,GPIO.LOW)
	GPIO.output(RedLED,GPIO.HIGH)
	#or the fast-way!
	#GPIO.output(LEDs[1],GPIO.HIGH)
	print("Red LED!")
	time.sleep(5)
	GPIO.output(RedLED,GPIO.LOW)
	GPIO.output(GreenLED,GPIO.HIGH)
	print("Green LED!")
	time.sleep(5)
	GPIO.output(GreenLED,GPIO.LOW)
	GPIO.output(BlueLED,GPIO.HIGH)
	print("Blue LED!")
	time.sleep(5)
