"""
Read sensor data from a AS7341 spectral sensor through a QT Py 2040 connected to your PC via USB

Inspired by https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
and
https://github.com/kavli-ntnu/wheel_tracker/blob/master/save_tracking.py
"""

import serial
import keyboard
from datetime import datetime

ser = serial.Serial('COM3') #The port to read from (i.e. the USB port the QT Py is connected to)
ser.flushInput() #This clears the serial buffer so everything is ready to go

# Specify which folder to save the data in
root_folder = 'C:/DATA/Sensor_data' 

# Get the current time
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Create a cvs file with a name based on the current time in the root folder specified 
output_file='{}/{}_spectra.csv'.format(root_folder, now)

# While this variable is True, values will be recorded
record = True

#If the key under keyboard.add_hotkey is pressed, this function is invoked and record is set to False
def stop_recording(): 
    global record #Make this variable global
    record=False
keyboard.add_hotkey('s', stop_recording) #Specify which key to press to stop recording values (default = s)

# Main code:
f = open(output_file,"a") #Open the csv file
f.write('Timestamp,415nm,445nm,480nm,515nm,555nm,590nm,630nm,680nm\n') #Add headers to the file

while record: #While record = True, run the following code to record and save light values in output_file
    
    ser_bytes = ser.readline() #Read one line from the port
    decoded_bytes = ser_bytes.decode('utf-8') #Convert the read data so it's legible
    decoded_bytes_split = decoded_bytes.strip().split(',') #Strip away the prefix and suffix characters, and split the values using the comma as the separator
    
    # Extract the different light values and convert them to floats
    value_415 = float(decoded_bytes_split[0])
    value_445 = float(decoded_bytes_split[1])
    value_480 = float(decoded_bytes_split[2])
    value_515 = float(decoded_bytes_split[3])
    value_555 = float(decoded_bytes_split[4])
    value_590 = float(decoded_bytes_split[5])
    value_630 = float(decoded_bytes_split[6])
    value_680 = float(decoded_bytes_split[7])

    # Get the current time
    now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
    
    # Print out the values in the terminal
    print('{} | 415nm: {} | 445nm: {} | 480nm: {} | 515nm: {} | 555nm: {} | 590nm: {} | 630nnm: {} | 680nm: {}'.format(
                                                now[0:-7],
                                                value_415,
                                                value_445,
                                                value_480,
                                                value_515,
                                                value_555,
                                                value_590,
                                                value_630,
                                                value_680))

    # Save the values in the csv file
    f.write('{},{},{},{},{},{},{},{},{}\n'.format(now,
                                                value_415,
                                                value_445,
                                                value_480,
                                                value_515,
                                                value_555,
                                                value_590,
                                                value_630,
                                                value_680))

f.close() #Close the file when 'record' is no longer True
print('Finished saving spectral values')