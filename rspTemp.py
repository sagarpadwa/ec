import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

while True:
    values = [0]*1
    
    for i in range(1):
        values[i] = adc.read_adc(i, gain=GAIN)
        temp = values[i] * 0.125
        temp = temp / 10

        print('Analog Input = {0:>6}'.format(*values))
        print('Temp in C = {0:0.2f}'.format(temp))
    
    time.sleep(2)
