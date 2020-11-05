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

# Dev1
dev1Window = WindowPane(tab1, HORIZONTAL)
dev1Window.pack(fill=BOTH, expand=1)
pw1 = WindowPane(dev1Window, VERTICAL)

afstandLabel1 = MyLabel(dev1Window, 'AFSTANDAFBEELDING 1')
temperatuurLabel1 = MyLabel(dev1Window, 'Temperatuur 1')
lichtLabel1 = MyLabel(dev1Window, 'Licht1')

dev1Window.addLabel(afstandLabel1, pw1)
pw1.addLabel(temperatuurLabel1, lichtLabel1)



#dev2Window = WindowPane(tab2)
#dev2Window.pack(fill=BOTH, expand=2)






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



# Widgets tab 1

# Window panes
# Pane 1
#dev1Window = PanedWindow(tab1)
#dev1Window.pack(fill=BOTH, expand=1)

#pw1 = PanedWindow(dev1Window, orient=VERTICAL)
#dev1Window.add(pw1)

#afstandLabel1 = Label(dev1Window, text='AFSTANDAFBEELDING1')
#dev1Window.add(afstandLabel1)

#top1 = Label(pw1, text='Temperatuur1')
#pw1.add(top1)

#bottom1 = Label(pw1, text='Licht1')
#pw1.add(bottom1)


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









mainFrame.mainloop()
