# Spectral_sensor
Save data from a AS7341 spectral sensor.

Save data from a [AS7341 spectral sensor](https://learn.adafruit.com/adafruit-as7341-10-channel-light-color-sensor-breakout) ([instructions](https://learn.adafruit.com/adafruit-as7341-10-channel-light-color-sensor-breakout/python-circuitpython)) connected to a [QT Py RP2040](https://www.adafruit.com/product/4900) with a [STEMMA QT cable](https://www.adafruit.com/product/4399) and your PC via USB.

<img src="QTPy_with_spectral_sensor.JPG" alt="QT Py with spectral sensor in front of a screen that displays the values being printed out" width="400"/>

## How it works
Values from 8 channels on the spectral sensor are saved continuously in a csv file on your computer until a specified key on your keyboard is pressed.

## Requirements
You need to have the python package [serial](https://pythonhosted.org/pyserial/) and [keyboard](https://github.com/boppreh/keyboard) installed in your environment.

## Setup and use instructions

- Connect the QT Py to your computer via USB
- Configure the QT Py according to [these instructions](https://learn.adafruit.com/adafruit-qt-py-2040/circuitpython) if you have not already done so
- Copy over the following to the "lib" folder on your CIRCUITPY (D:) drive from one of the [CircuitPython library bundles](https://circuitpython.org/libraries):

  **Files:**
  - adafruit_AS7341.mpy
  - neopixel.mpy

  **Folders:**
  - adafruit_bus_device
  - adafruit_register

- Connect the spectral sensor to the QT Py with the STEMMA QT cable
- Copy the contents of the *code.py* file in this repository into the *code.py* file on your CIRCUITPY (D:) drive. The LED on the QT Py will turn off to indicate that the code is running
- Specify which USB port the QT Py is connected to by modifying the 'ser' variable within *serial_reader.py* (default port: COM3)
- Specify which folder the csv file should be saved in on your PC by modifying the 'root_folder' variable within *serial_reader.py* (default location: C:/DATA/Sensor_data)
- Run the *serial_reader.py* file in your terminal to start recording light values. These will also be printed out in your terminal
- Press the 's' key on your keyboard while in your terminal to stop recording values (you can modify which key to press to stop the code by modifying the first argument in 'keyboard.add_hotkey' in *serial_reader.py*)
- A csv file with the recorded values and timestamps can now be found in the location you specified
