#!/usr/bin/env python3
"""Serial read from arduino
"""
from serial.tools import list_ports
import serial
import time


ports = list_ports.comports()
for port in ports: print(port)

serialCom = serial.Serial('COM10', 9600)
serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)

while 1:
    s_bytes = serialCom.readline()
    data = s_bytes.decode('utf-8').strip('\r\n')
    print(data)