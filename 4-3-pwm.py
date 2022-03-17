import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pwmi  = 22
GPIO.setup(pwmi, GPIO.OUT)

pwm = GPIO.PWM(pwmi, 60)
pwm.ChangeDutyCycle(0.5) 
try:
    GPIO.setup(12, GPIO.OUT)    
    pwm.start(1)
    while (1):
        pwm.ChangeDutyCycle(float(input()))

finally:
    pwm.stop()
    GPIO.cleanup()
