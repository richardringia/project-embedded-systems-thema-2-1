import serial
import time

ser = serial.Serial('COM3', 19200, timeout=1)

print(ser)

while True:

    ser.write(bytes("5#".encode()))
    read_val = ser.read()
    print(read_val)
