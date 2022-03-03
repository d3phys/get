import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.OUT)

while True:
    GPIO.output(15, 0)
  
    GPIO.output(15, 1)
    