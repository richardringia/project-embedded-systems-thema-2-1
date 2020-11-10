import connect
from device import Device
from gui import *
from threading import Thread

devices = []
threads = []

for device in connect.get_devices():

    main = Main(device, tabControl)
    device.set_main(main)
    thread = Thread(target=device.loop)
    thread.start()
    threads.append(thread)
    devices.append(device)
    threads.append(device.timer)
    threads.append(device.updater)

mainFrame.addDevices(devices)

mainFrame.mainloop()

for thread in threads:
    thread.join()

print('closed')
