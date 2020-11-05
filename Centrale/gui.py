import tkinter as tk
from tkinter import *
from tkinter import ttk

# Define main window
mainWindow = Tk()
mainWindow.title("Central Control Unit")
mainWindow.geometry("500x500")



# Define tabs
tabControl = ttk.Notebook(mainWindow)

# tab 1
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Device 1')
tabControl.pack(expand=1, fill='both')

# tab 2
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Device 2')
tabControl.pack(expand=1, fill='both')


# TESTTESTTEST (widgets tab1)
#testLabelTab1 = Label(tab1, text='testnaam')
#testEntryTab1 = Entry(tab1)
#testLabelTab1.pack(fill=BOTH, expand = 1)


# Widgets tab 1


# Window panes
# Pane 1
dev1Window = PanedWindow(tab1)
dev1Window.pack(fill=BOTH, expand=1)

afstandLabel1 = Label(dev1Window, text='AFSTANDAFBEELDING1')
dev1Window.add(afstandLabel1)

pw1 = PanedWindow(dev1Window, orient=VERTICAL)
dev1Window.add(pw1)

top1 = Label(pw1, text='Temperatuur1')
pw1.add(top1)

bottom1 = Label(pw1, text='Licht1')
pw1.add(bottom1)


# Pane 2
dev2Window = PanedWindow(tab2)
dev2Window.pack(fill=BOTH, expand=1)

afstandLabel2 = Label(dev2Window, text="AFSTANDAFBEELDING2")
dev2Window.add(afstandLabel2)

pw2 = PanedWindow(dev2Window, orient=VERTICAL)
dev2Window.add(pw2)

top2 = Label(pw2, text='Temperatuur2')
pw2.add(top2)

bottom2 = Label(pw2, text='Licht2')
pw2.add(bottom2)









mainWindow.mainloop()
