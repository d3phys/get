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

def adc_sar():
    step    = 2**7
    voltage = step
    while step:
        GPIO.output(dac, dec2bin(voltage))
        time.sleep(0.001)
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

    return voltage

try:
    while True:
        print("SAR")
        time.sleep(2)
        for i in range(25):
            val = adc_sar()
            print("Voltage: {:.2f} V".format(val * 3.3 / 256))


        print("Simple")    
        time.sleep(2)

        for i in range(25):
            val = adc()
            print("Voltage: {:.2f} V".format(val * 3.3 / 256))
        



finally:
    print("Bye-bye")
    GPIO.output(dac, 0)
    GPIO.cleanup()
