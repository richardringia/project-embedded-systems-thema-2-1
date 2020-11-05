# Connect with the arduino's

import serial.tools.list_ports
import serial
import sys



def get_devices():
    ports = serial.tools.list_ports.comports()
    devices = []
    if sys.platform.startswith('win'):
        # todo: check devices from windows
        pass
    elif sys.platform.startswith('darwin'):
        for port in ports:
            if port.device.startswith('/dev/cu.usbmodem'):
                devices.append(port.device)
        pass
    else:
        raise EnvironmentError('Unsupported platform')

    return devices

for device in get_devices():
    ser = serial.Serial(device, 192000, timeout=1)
    
    while True:
        ser.write(bytes("abc".encode()))
        read_val = str(ser.readline())
        print(ser.read_all())