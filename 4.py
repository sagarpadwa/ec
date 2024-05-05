import RPi.GPIO as GPIO
import time

# Disable GPIO warnings 4 
GPIO.setwarnings(False)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for LEDs
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

try:
    while True:
        # LED 1
        GPIO.output(4, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(4, GPIO.LOW)
        
        # LED 2
        GPIO.output(17, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(17, GPIO.LOW)
        
        # LED 3
        GPIO.output(18, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(18, GPIO.LOW)
        
        # LED 4
        GPIO.output(27, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(27, GPIO.LOW)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
