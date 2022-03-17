import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
    
dac = [26, 19, 13, 6, 5, 11, 9, 10]
steps = 255

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def triangle(period):
    dt = period / (2 * steps)
    for i in range(steps):
        GPIO.output(dac, dec2bin(i))
        time.sleep(dt)

    for i in range(steps, 0, -1):
        GPIO.output(dac, dec2bin(i))
        time.sleep(dt)

    return 0

try:
    period = int(input("Enter:"))
    while(1):
        triangle(period)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()