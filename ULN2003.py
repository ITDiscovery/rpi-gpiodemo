#From https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/
#Corrected for the motor in the demo
#Need to add error handling turn off motor after Ctrl-C

import RPi.GPIO as GPIO
import time
# Setup for signal handling, cleanup on Ctrl-C
import signal
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
coil_A_1_pin = 24 # pink
coil_A_2_pin = 26 # orange
coil_B_1_pin = 19 # blue
coil_B_2_pin = 18 # yellow

# adjust if different motor
# Very important to match phase steps
StepCount = 8
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def sigint_handler(signum, frame):
    GPIO.output(coil_A_1_pin,GPIO.LOW)
    GPIO.output(coil_A_2_pin,GPIO.LOW)
    GPIO.output(coil_B_1_pin,GPIO.LOW)
    GPIO.output(coil_B_2_pin,GPIO.LOW)
    print("Exit Signal Recieved!")
    GPIO.cleanup
    exit()

signal.signal(signal.SIGINT, sigint_handler)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
if __name__ == '__main__':
    while True:
        #delay = raw_input("Time Delay (ms)?")
        #steps = raw_input("How many steps forward? ")
        print("Forward 300 Steps")
        delay=1.5
        steps=500
        forward(int(delay) / 1000.0, int(steps))
        #steps = raw_input("How many steps backwards? ")
        print("Backward 300 Steps")
        delay=1.5
        steps=500
        backwards(int(delay) / 1000.0, int(steps))
