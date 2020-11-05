from tkinter import *
from tkinter import ttk


class MainFrame(Tk):

    def __init__(self):
        super().__init__()
        self.title('Central Control Unit')
        self.geometry('750x750')


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


class MyButton(Button):

    def __init__(self, parent, text):
        super().__init__(parent, text=text)
        self.config(height=1, width=50)


class MyEntry(Entry):

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


# Dev1 Tab
dev1Tab = WindowPane(tab1, HORIZONTAL)
dev1Tab.pack(fill=BOTH, expand=1)
pw1 = WindowPane(dev1Tab, VERTICAL)
pw2 = WindowPane(dev1Tab, VERTICAL)

afstandLabel1 = MyLabel(dev1Tab, 'AFSTAND AFBEELDING 1')
instellingenLabel1 = MyLabel(dev1Tab, 'Instellingen 1')
temperatuurLabel1 = MyLabel(dev1Tab, 'Temperatuur 1')
lichtLabel1 = MyLabel(dev1Tab, 'Licht 1')

dev1Tab.addLabel(pw1, pw2)
pw1.addLabel(afstandLabel1, instellingenLabel1)
pw2.addLabel(temperatuurLabel1, lichtLabel1)


#afstandEntry1 = Entry(dev1Tab)
#temperatuurEntry1 = Entry(dev1Tab)

btn1 = MyButton(dev1Tab, 'Instellen!')
pw1.addLabel(btn1)


# Dev2 Tab
dev2Tab = WindowPane(tab2, HORIZONTAL)
dev2Tab.pack(fill=BOTH, expand=1)
pw3 = WindowPane(dev2Tab, VERTICAL)
pw4 = WindowPane(dev2Tab, VERTICAL)

afstandLabel2 = MyLabel(dev2Tab, 'AFSTAND AFBEELDING 2')
instellingenLabel2 = MyLabel(dev2Tab, 'Instellingen 2')
temperatuurLabel2 = MyLabel(dev2Tab, 'Temperatuur 2')
lichtLabel2 = MyLabel(dev2Tab, 'Licht 2')

dev2Tab.addLabel(pw3, pw4)
pw3.addLabel(afstandLabel2, instellingenLabel2)
pw4.addLabel(temperatuurLabel2, lichtLabel2)


mainFrame.mainloop()
