import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(4, GPIO.OUT)

while True:
    button_state = GPIO.input(17)

    if button_state == True:
        GPIO.output(4, False)
        print('Motion Detected...')
        while GPIO.input(17) == True:
            time.sleep(0.2)
    else:
        GPIO.output(4, True)