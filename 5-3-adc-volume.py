import RPi.GPIO as GPIO
import time

dac  = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc_sar():
    step    = 2**7
    voltage = step
    while step:
        GPIO.output(dac, dec2bin(voltage))
        time.sleep(0.007)
        if GPIO.input(comp) == 0:
            voltage -= step 
        
        step   >>= 1
        voltage += step

    return voltage

def adc():
    for voltage in range(255):
        GPIO.output(dac, dec2bin(voltage))
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            return voltage

def dec2range(value):
    count = round(value / 32)
    list = (8 - count) * [0] + count * [1]
    return list

try:
    while True:
        voltage = adc_sar()
        print("Voltage: {:.2f} V".format(voltage * 3.3 / 256))
        GPIO.output(leds, dec2range(voltage))

finally:
    print("Bye-bye")
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
