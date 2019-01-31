#Stepper Motor Test via ULN2003AN
#ULN2003A Drive Voltage on 9, Gnd on 8
#Using GPIO2 on pin 1 of ULN2003 to drive motor on pin 16
#Using GPIO17 to drive indicator LED 

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# Set 2 for Data out Motor Drive
GPIO.setup(2,GPIO.OUT)
# Set 3 for Data out Motor Drive
GPIO.setup(3,GPIO.OUT)

# Set 17 for Data Out
GPIO.setup(17,GPIO.OUT, initial=False)

while True:
    GPIO.output(2,True)
    GPIO.output(17,True)
    time.sleep(2)
    GPIO.output(2,False)
    GPIO.output(17,False)
    time.sleep(2)
    
