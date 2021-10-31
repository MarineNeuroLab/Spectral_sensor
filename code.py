# Print out values from 8 sensors on an AS7341 spectral sensor
# Description: https://learn.adafruit.com/adafruit-as7341-10-channel-light-color-sensor-breakout/python-circuitpython

#from time import sleep #Use if necessary (see last line in this file)
import board
import busio
import adafruit_as7341
import neopixel

i2c = busio.I2C(board.SCL1,board.SDA1)  # Create sensor object
sensor = adafruit_as7341.AS7341(i2c)  # Initialise the sensor
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1) # Instantiate QT Py neopixel LED

### WHITE LED OPTIONS ################################################
#sensor.led_current = 1 #Set the current of the white LED on the sensor (i.e. set the brightness)
#sensor.led = True #Turn the white LED on for 0.5 seconds and then off again
#sleep(0.5)
#sensor.led = False
######################################################################

# Main code
pixels[0] = (0, 0, 0)  #Turn off the QT Py neopixel to indicate that the code is running

while True: #Do the following continuously:
    """   
    Available channels:
    print("F1 - 415nm/Violet  %s" % sensor.channel_415nm)
    print("F2 - 445nm//Indigo %s" % sensor.channel_445nm)
    print("F3 - 480nm//Blue   %s" % sensor.channel_480nm)
    print("F4 - 515nm//Cyan   %s" % sensor.channel_515nm)
    print("F5 - 555nm/Green   %s" % sensor.channel_555nm)
    print("F6 - 590nm/Yellow  %s" % sensor.channel_590nm)
    print("F7 - 630nm/Orange  %s" % sensor.channel_630nm)
    print("F8 - 680nm/Red     %s" % sensor.channel_680nm)
    """
    # Print out the values that should be kept to the serial port
    print("{},{},{},{},{},{},{},{}".format(sensor.channel_415nm, 
                                            sensor.channel_445nm, 
                                            sensor.channel_480nm,
                                            sensor.channel_515nm,
                                            sensor.channel_555nm,
                                            sensor.channel_590nm,
                                            sensor.channel_630nm,
                                            sensor.channel_680nm))
    
    #sleep(0.5) #Introduce a delay if you want readings to be taken at a set rate