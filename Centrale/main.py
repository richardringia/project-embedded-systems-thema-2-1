import connect
from device import Device
from gui import *
from threading import Thread


mainFrame = MainFrame()
tabControl = TabControl(mainFrame)
tabControl.grid(row=0)

devices = []
threads = []

for device in connect.get_devices():
    main = Main(device.port)
    tabControl = main.createTab(tabControl)
    device.set_main(main)
    thread = Thread(target=device.loop)
    thread.start()
    threads.append(thread)
    devices.append(device)
    threads.append(device.timer)

mainFrame.addDevices(devices)

mainFrame.mainloop()

for thread in threads:
   thread.join()

print('closed')