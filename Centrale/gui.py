from tkinter import *
from tkinter import ttk


class MainFrame(Tk):

    def __init__(self):
        super().__init__()
        self.title('Central Control Unit')
        self.geometry('500x500')


class TabControl(ttk.Notebook):

    def __init__(self, mainframe):
        super().__init__(mainframe)

    def addTabs(self, *tabs):
        #placeholder
        for tab in tabs:
            self.add(tab, text=tab.name)


class Tab(ttk.Frame):

    def __init__(self, tabcontrol, name):
        super().__init__(tabcontrol)
        self.name = name


class WindowPane(PanedWindow):

    def __init__(self, parent, orient):
        super().__init__(parent, orient=orient)

    def addLabel(self, *labels):
        #placeholder
        for label in labels:
            self.add(label)


class MyLabel(Label):

    def __init__(self, parent, text):
        super().__init__(parent, text=text)


# Definitions
mainFrame = MainFrame()
# Tabs
tabControl = TabControl(mainFrame)
tab1 = Tab(tabControl, 'Device 1')
tab2 = Tab(tabControl, 'Device 2')
tabControl.addTabs(tab1, tab2)
tabControl.pack(expand=1, fill='both')


# Dev1 tab
dev1Window = WindowPane(tab1, HORIZONTAL)
dev1Window.pack(fill=BOTH, expand=1)
pw1 = WindowPane(dev1Window, VERTICAL)

afstandLabel1 = MyLabel(dev1Window, 'AFSTANDAFBEELDING 1')
temperatuurLabel1 = MyLabel(dev1Window, 'Temperatuur 1')
lichtLabel1 = MyLabel(dev1Window, 'Licht 1')

dev1Window.addLabel(afstandLabel1, pw1)
pw1.addLabel(temperatuurLabel1, lichtLabel1)


# Dev2 tab
dev2Window = WindowPane(tab2, HORIZONTAL)
dev2Window.pack(fill=BOTH, expand=1)
pw2 = WindowPane(dev2Window, VERTICAL)

afstandLabel2 = MyLabel(dev2Window, 'AFSTANDAFBEELDING 2')
temperatuurLabel2 = MyLabel(dev2Window, 'Temperatuur 2')
lichtLabel2 = MyLabel(dev2Window, 'Licht 2')

dev2Window.addLabel(afstandLabel2, pw2)
pw2.addLabel(temperatuurLabel2, lichtLabel2)


mainFrame.mainloop()
