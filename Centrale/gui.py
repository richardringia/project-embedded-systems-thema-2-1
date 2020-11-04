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


#Window panes
dev1Window = PanedWindow(tab1)
dev1Window.pack(fill=BOTH, expand=1)

afstandLabel = Label(dev1Window, text='AFSTANDAFBEELDING')
dev1Window.add(afstandLabel)

m2 = PanedWindow(dev1Window, orient=VERTICAL)
dev1Window.add(m2)

top = Label(m2, text='Temperatuur')
m2.add(top)

bottom = Label(m2, text='Licht')
m2.add(bottom)











mainWindow.mainloop()
