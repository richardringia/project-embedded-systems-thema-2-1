import serial
import time

ser = serial.Serial('COM3', 19200, timeout=1)

print(ser)

while True:
    #value = input("LED On or [Off]:\n")

    #if value == "On":
    #    ser.write(bytes("1".encode()))
    #else:
    #    ser.write(bytes("0".encode()))

    ser.write(bytes("kaasje".encode()))
        
    read_val = str(ser.readline())
    print(read_val)
