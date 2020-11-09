import connect
from device import Device
from gui import *
from threading import Thread

# device = connect.get_devices()[0]
# while True:
    # print(device.get_temp())

mainFrame = MainFrame()
tabControl = TabControl(mainFrame)
tabControl.grid(row=0)

devices = []
threads = []

for device in connect.get_devices():
    main = Main(device.port)
    tabControl = main.createTab(tabControl)
    thread = Thread(target=device.loop)
    thread.start()
    threads.append(thread)
    devices.append(device)

mainFrame.addDevices(devices)

mainFrame.mainloop()

for thread in threads:
   thread.join()

