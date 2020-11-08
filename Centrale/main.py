import serial

from device import Device
import connect


device = connect.get_devices()[0]
# while True:
    # print(device.get_temp())