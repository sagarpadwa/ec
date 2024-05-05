#Feedback Switch
import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Push button
GPIO.setup(4, GPIO.OUT)  # LED

while True:
    button_state = GPIO.input(17)
    
    if button_state == False:
        GPIO.output(4, False)
        print("Button pressed...")
        while GPIO.input(17) == False:
            time.sleep(0.2)
    else:
        GPIO.output(4, True)
        
#2
import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Push button 1
GPIO.setup(4, GPIO.OUT)                             # LED 1
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Push button 2
GPIO.setup(18, GPIO.OUT)                            # LED 2

while True:
    button1_state = GPIO.input(17)
    button2_state = GPIO.input(27)
    
    if button1_state == False:
        GPIO.output(4, False)
        print('Button 1 pressed...')
        while GPIO.input(17) == False:
            time.sleep(0.2)
    else:
        GPIO.output(4, True)
    
    if button2_state == False:
        GPIO.output(18, False)
        print('Button 2 pressed...')
        while GPIO.input(27) == False:
            time.sleep(0.2)
    else:
        GPIO.output(18, True)

