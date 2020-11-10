import serial
import time
from threading import Thread

class Device:
  running = True
  counter = 0
  timer = None
  updater = None
  main = None
  data_to_send = None
  update_settings = 0

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
      time.sleep(1)    

  def run_update_settings(self):
    while self.running:
      if (self.update_settings == 1):
        self.send("5" + self.main.MinTemperatuur + "#")
        time.sleep(1)
        self.send("6" + self.main.MaxTemperatuur + "#")
        time.sleep(1)
        self.send("7" + self.main.MinLicht + "#")
        time.sleep(1)
        self.send("8" + self.main.MaxLicht + "#")
        time.sleep(1)   
        self.update_settings = 0

  def send(self, data):
    self.data_to_send = data

  def loop(self):
    self.timer = Thread(target=self.run_counter)
    self.timer.start()

    self.updater = Thread(target=self.run_update_settings)
    self.updater.start()

    recieve_data = False
    recieve_data_type = None
    #recieve_data_value = None

    while self.running:
      self.serial.write(bytes(str(self.counter).encode()))
      if self.data_to_send != None:
        self.serial.write(bytes(str(self.data_to_send).encode()))
        self.data_to_send = None
      serial_data = int.from_bytes(self.serial.read(), byteorder='little')
      if serial_data == 1:
        recieve_data = True
      elif serial_data != 0 and recieve_data and recieve_data_type == None: # lezen welke data
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

          self.main.setImage(status)
        elif recieve_data_type == 9:
          print(serial_data)

        #reset
        recieve_data = False
        recieve_data_type = None

      #print(serial_data)

         