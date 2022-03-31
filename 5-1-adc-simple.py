import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    for voltage in range(255):
        GPIO.output(dac, dec2bin(voltage))
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            return voltage

    return voltage

try:
    while(True):
        voltage = adc()
        print("Voltage: {:.2f} V".format(voltage * 3.3 / 256))

finally:
    print("Bye-bye")
    GPIO.output(dac, 0)
    GPIO.cleanup()

