#for 1 LED
import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 4 as an output
GPIO.setup(4, GPIO.OUT)

try:
    while True:
        GPIO.output(4, GPIO.HIGH)  # Turn the LED on
        time.sleep(3)  # Wait for 3 seconds
        GPIO.output(4, GPIO.LOW)   # Turn the LED off
        time.sleep(3)  # Wait for 3 seconds

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
    
import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
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

