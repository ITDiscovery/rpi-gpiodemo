#Bi-Directional Motor Test via L298N
#Using GPIO 12 for forward and 16 for backward

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

# Set 2 for Data out Motor Drive
GPIO.setup(16,GPIO.OUT)
# Set 3 for Data out Motor Drive
GPIO.setup(18,GPIO.OUT)

while True:
    GPIO.output(16,True)
    GPIO.output(18,False)
    time.sleep(10)
    GPIO.output(16,False)
    GPIO.output(18,True)
    time.sleep(2)
    
