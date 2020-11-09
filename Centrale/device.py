import serial
import time
from threading import Thread

class Device:
  running = True
  counter = 0
  timer = None
  main = None

  def __init__(self, port):
    self.port = port
    self.serial = serial.Serial(port, 19200, timeout=1)
    # while True:
    #   self.serial.write(bytes("0".encode()))
    #   serial_data = int.from_bytes(self.serial.read(), byteorder='little')
    #   print(serial_data)

  def stop(self):
    self.running = False

  def set_main(self, main):
    self.main = main

  def run_counter(self):
    while self.running:
      if (self.counter == 1):
        self.counter = 0
      else:
        self.counter = 1
      print(self.counter)
      time.sleep(1)      

  def loop(self):
    self.timer = Thread(target=self.run_counter)
    self.timer.start()

    recieve_data = False
    recieve_data_type = None
    #recieve_data_value = None

    while self.running:
      self.serial.write(bytes(str(self.counter).encode()))
      serial_data = int.from_bytes(self.serial.read(), byteorder='little')
      if serial_data == 1:
        print('data recieved')
        recieve_data = True
      elif serial_data != 0 and recieve_data and recieve_data_type == None: # lezen welke data
        print('data type recieved')
        recieve_data_type = serial_data
      elif recieve_data and recieve_data_type != None:
        #recieve_data_value = serial_data
        if recieve_data_type == 2:
          self.main.drawTemperature(serial_data)
        elif recieve_data_type == 3:
          self.main.drawLight(serial_data)
        elif recieve_data_type == 4:
          # 0, 20, 40, 60, 80, 100
          status = 0
          if serial_data <= 10:
            status = "0"
          elif serial_data > 10 and serial_data <= 30:
            status = "20"
          elif serial_data > 30 and serial_data <= 50:
            status = "40"
          elif serial_data > 50 and serial_data <= 70:
            status = "60"
          elif serial_data > 70 and serial_data <= 90:
            status = "80"
          elif serial_data > 90:
            status = "100"

          self.main.setImage("zonnescherm" + status + ".png")

        #reset
        recieve_data = False
        recieve_data_type = None

      #print(serial_data)
    


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



         