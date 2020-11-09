# Connect with the arduino's

import serial.tools.list_ports
import serial
import sys
import time
from device import *

def get_devices():
   
    ports = serial.tools.list_ports.comports()
    devices = []
    if sys.platform.startswith('win'):
        for port in ports:
            devices.append(Device(port.device))
    elif sys.platform.startswith('darwin'):
        for port in ports:
            if port.device.startswith('/dev/cu.usbmodem'):
                devices.append(Device(port.device))
        pass
    elif sys.platform.startswith('Linux') or sys.platform.startswith('linux'):
        for port in ports:
            devices.append(Device(port.device))
    else:
        raise EnvironmentError('Unsupported platform')

    return devices