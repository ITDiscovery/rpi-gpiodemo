#Servo Motor Test via SG-90 5V servo
#Using Pin 22 for PWM connection
#From IanC1999 at https://www.instructables.com/id/Serv-Motor-Control-With-Rasperry PI/

import RPi.GPIO as GPIO
import time
# Setup for signal handling, cleanup on Ctrl-C
import signal
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
Srvo=22

# Set of Data out Motor Drive
GPIO.setup(Srvo,GPIO.OUT)
freq = GPIO.PWM(Srvo,50)
freq.start(0)

def SetAngle(angle):
	duty = ((1/18.0)*angle) +2
	#print(duty)
	#Turn on the Pin
	GPIO.output(Srvo,True)
	#Move the motor to the spot
	freq.ChangeDutyCycle(duty)
	#Wait for move
	time.sleep(2)
	#Turn off the Pin
	GPIO.output(Srvo,False)
	#Stop sending pulses
	freq.ChangeDutyCycle(0)

def sigint_handler(signum, frame):
	GPIO.cleanup
	print("Signal recieved, exiting!")
	exit()

signal.signal(signal.SIGINT, sigint_handler)

def main():
	while True:
		print("Setting to 0")
		SetAngle(0)
		print("Setting to 180")
		SetAngle(180)
		print("Setting to 45")
		SetAngle(45)
		print("Setting to 225")
		SetAngle(225)
		print("Setting to 90")
		SetAngle(90)

if __name__=="__main__":
	main()
