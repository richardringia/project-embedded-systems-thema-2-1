import serial

class Device:

    def __init__(self, port):
        self.serial = serial.Serial(port, 19200, timeout=1)
        
    def get_temp(self):
        return self.__get_value("0")
        
    def get_light(self):
        return self.__get_value("1")
        
    def get_distance(self):
        return self.__get_value("2")

    # Get value from the uart
    def __get_value(self, type):
        counter = 0
        value = b''
        while value == b'' and counter < 6:
            self.serial.write(bytes(type.encode()))
            value = self.serial.readline()
            counter +=1
        
        return value



         