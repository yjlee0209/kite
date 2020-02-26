#coding: utf-8

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

TRIG = 18
ECHO = 25

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        stop = 0
        start = 0

        GPIO.output(TRIG, False)
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.0001)
        GPIO.output(TRIG, False)
    
        while GPIO.input(ECHO)==0:
            start = time.time()
  
        while GPIO.input(ECHO)==1:
            stop = time.time()
 
        elapsed = stop-start
        
        if (stop and start):
            distance = (elapsed * 34000.0) / 2
            print("Distance : %.1f cm" % distance)

except KeyboardInterrupt:   
    print("Ultrasonic Distance Measurement End")
    GPIO.cleanup()
 
GPIO.cleanup()