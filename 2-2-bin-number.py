import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


GPIO.output(dac, 0)
GPIO.cleanup()

GPIO.output(dac, 0)
#time.sleep(7)

input = [255, 127, 64, 32, 5, 0, 256]
volt = [3.261, 1.627, 0.824, 0.501, 0.486, 0.486, 0.486]

#plt.scatter(input, volt)
#plt.savefig('plot.pdf')

def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

for i in input:
    GPIO.output(dac, binary(i))
    time.sleep(7)



GPIO.output(dac, 0)
GPIO.cleanup()



