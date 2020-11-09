import connect
from device import Device
from gui import *

# device = connect.get_devices()[0]
# while True:
    # print(device.get_temp())

mainFrame = MainFrame()
tabControl = TabControl(mainFrame)
tabControl.grid(row=0)

for device in connect.get_devices():
    main = Main(device.port)
    device.loop()

mainFrame.mainloop()