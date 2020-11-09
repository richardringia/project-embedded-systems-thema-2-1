import serial
import time

class Device:
  running = True
  def __init__(self, port):
    self.port = port
    self.serial = serial.Serial(port, 19200, timeout=1)
    # while True:
    #   self.serial.write(bytes("0".encode()))
    #   serial_data = int.from_bytes(self.serial.read(), byteorder='little')
    #   print(serial_data)

  def stop(self):
    self.running = False

  def loop(self):
    while self.running:
      print(self.port)
      time.sleep(1)

 
    


    # def __init__(self, port):
    #     self.serial = serial.Serial(port, 19200, timeout=1)
        
    # def get_temp(self):
    #   return self.__get_value("0")
        
    #def get_light(self):
  #      return self.__get_value("1")
        
    #def get_distance(self):
    #    return self.__get_value("2")

    # # Get value from the uart
    # def __get_value(self, type):
    #     counter = 0
    #     value = b''
    #     while (value == b'' or value == b'0') and counter < 6:
    #       self.serial.write(bytes(type.encode()))
    #       value = self.serial.readline()
    #       counter +=1
        
    #     return str(value, 'utf-8')



         