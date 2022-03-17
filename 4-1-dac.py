import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
    
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def predict(value):
    return int(value) / 2**8 * 3.3

try:
    ui = input("Enter number: ")

    if (ui.isdigit() and 0 < int(ui) < 2**8):
        num = int(ui)
        GPIO.output(dac, dec2bin(num))
        print(predict(ui))
        time.sleep(2)
    elif (ui != 'q'):
        raise Exception()

except Exception:
    print("Error")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
