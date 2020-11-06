import serial
import time
import connect
import threading



array_temp = dict()
array_light = dict()

device = connect.get_devices()[0]

def get_temp_every_60_sec():
    threading.Timer(60.0, get_temp_every_60_sec).start() # called every minute
    print(device.get_temp())

get_temp_every_60_sec()
# print(device.get_temp())