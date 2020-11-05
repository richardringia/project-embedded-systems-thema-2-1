# Connect with the arduino's

import serial.tools.list_ports
import serial
import sys
import time



def get_devices():
    ports = serial.tools.list_ports.comports()
    devices = []
    if sys.platform.startswith('win'):
        for port in ports:
            devices.append(port.device)
    elif sys.platform.startswith('darwin'):
        for port in ports:
            if port.device.startswith('/dev/cu.usbmodem'):
                devices.append(port.device)
        pass
    else:
        raise EnvironmentError('Unsupported platform')

    return devices



for device in get_devices():
    
    ser = serial.Serial(device, 19200, timeout=1)
        
    while True:    
        ser.write(bytes("2".encode()))
        
        read_val = str(ser.readline())
        print(read_val)



    #print(device)
    
    # while True:
    #     #ser.write(bytes("abc".encode()))
    #     read_val = str(ser.readline())
    #     #read_val = bytes(ser.readline(), 'utf-8')
    #     print(read_val)