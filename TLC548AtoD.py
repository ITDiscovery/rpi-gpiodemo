#Bi-Directional Motor Test via L298N
#Using GPIO 12 for forward and 16 for backward

import RPi.GPIO as GPIO
import time
# Setup for signal handling, cleanup on Ctrl-C
import signal
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
Clk=8
DIO=10

# Set of Data out Analog to Digital Chip
GPIO.setup(Clk,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(DIO,GPIO.IN)

def sigint_handler(signum, frame):
    #GPIO.output(Dirs[0],GPIO.LOW)
    #GPIO.output(Dirs[1],GPIO.LOW)
    print("Exit Signal Recieved!")
    GPIO.cleanup
    exit()

signal.signal(signal.SIGINT, sigint_handler)

def tlc548RX():
    byte = 0
    for x in range(8):
        GPIO.output(Clk,GPIO.HIGH)
        byte = byte + ((2**x) * GPIO.input(DIO))
        GPIO.output(Clk,GPIO.LOW)
    return(byte)

def main():
    while True:
	time.sleep(.1)
	print(tlc548RX())
	#volt = (tlc548RX()/255)*5
        #print "Voltage: {0:5.4f}".format(volt)

if __name__=="__main__":
    main()
