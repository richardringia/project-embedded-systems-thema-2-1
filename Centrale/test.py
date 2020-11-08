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

#get_temp_every_61_sec()
# print(device.get_temp())

def get_temp_test():
    starttime = time.time() # sets the starttime to the current time
    print(device.get_temp()) # print the current temperature:w
    time.sleep(10.0 - ((time.time() - starttime) % 60)) # waits 60 seconds


"""
TEST LOOP 
"""

for i in range(0,3):
    get_temp_test()