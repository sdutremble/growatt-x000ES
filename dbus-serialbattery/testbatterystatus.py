# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals


import serial

command_firmware_version = b"\x7E\x01\x33\x00\xFE\x0D"
ser = serial.Serial("COM4", 9600, "N", 8, 1)
   
# Send character 'S' to start the program
ser.write(command_firmware_version)

# Read line   
while True:
bs = ser.readline()
print(bs)

