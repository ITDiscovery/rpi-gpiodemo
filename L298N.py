#Bi-Directional Motor Test via L298N
#Using GPIO 12 for forward and 16 for backward

import RPi.GPIO as GPIO
import time
# Setup for signal handling, cleanup on Ctrl-C
import signal
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
Dirs=[12,16]

# Set of Data out Motor Drive
GPIO.setup(Dirs,GPIO.OUT,initial=GPIO.LOW)

def sigint_handler(signum, frame):
	GPIO.output(Dirs[0],GPIO.LOW)
	GPIO.output(Dirs[1],GPIO.LOW)
	GPIO.cleanup
	print("Signal recieved, exiting!")
	exit()

signal.signal(signal.SIGINT, sigint_handler)

def main():
	while True:
		GPIO.output(Dirs[0],GPIO.HIGH)
		GPIO.output(Dirs[1],GPIO.LOW)
		print("Forward!")
		time.sleep(5)
		GPIO.output(Dirs[0],GPIO.LOW)
		GPIO.output(Dirs[1],GPIO.HIGH)
		print("Backward!")
		time.sleep(5)

if __name__=="__main__":
	main()
