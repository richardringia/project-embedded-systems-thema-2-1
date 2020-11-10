import serial
import time

ser = serial.Serial('COM3', 19200, timeout=1)

print(ser)

while True:

    ser.write(bytes("49#".encode()))
    read_val = ser.read()

    print(read_val)

    print(list(read_val))
