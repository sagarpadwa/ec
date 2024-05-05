import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

while True:
    values = [0] * 4  # Changed from 1 to 4 to match ADS1115 channels

    for i in range(4):  # Changed range from 1 to 4
        values[i] = adc.read_adc(i, gain=GAIN)

        if values[i] > 3000:
            print('Dark condition')
        else:
            print('Illuminated condition...')

    time.sleep(2)