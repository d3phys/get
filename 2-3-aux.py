import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while True:
    time.sleep(0.5)
    for pin in range(len(aux)):
        GPIO.output(dac[pin], GPIO.input(aux[pin]))
