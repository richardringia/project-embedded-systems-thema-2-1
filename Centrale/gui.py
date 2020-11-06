from tkinter import *
from tkinter import ttk
from graph import *


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

    def addTab(self, tab):
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
            self.add(label, stretch="always", height=375, width=375)


class MyLabel(Label):

    def __init__(self, parent, text):
        super().__init__(parent, text=text)


class MyButton(Button):

    def __init__(self, text):
        super().__init__(text=text)
        #self.config(height=50, width=50)


class MyEntry(Entry):

    def __init__(self, parent, text):
        super().__init__(parent, text=text)


# Definitions
mainFrame = MainFrame()
tabControl = TabControl(mainFrame)
tabControl.grid(row=0)


def createTab(name):
    tab = Tab(tabControl, name)
    tabControl.addTab(tab)

    devTab = WindowPane(tab, HORIZONTAL)
    devTab.grid(row=0, rowspan=10, column=0)

    pw1 = WindowPane(devTab, VERTICAL)
    pw1.config(bg='black')

    pw2 = WindowPane(devTab, VERTICAL)
    pw2.config(bg='black')

    afstandLabel = MyLabel(pw1, 'AFSTAND')
    instellingenLabel = MyLabel(pw1, 'INSTELLINGEN')
    temperatuurLabel = MyLabel(pw2, 'TEMPERATUUR')
    lichtLabel = MyLabel(pw2, 'LICHT')

    devTab.addLabel(pw1, pw2)
    pw1.addLabel(afstandLabel, instellingenLabel)
    pw2.addLabel(temperatuurLabel, lichtLabel)

    btn = MyButton('Instellen!')
    pw1.addLabel(btn)


createTab('Device 1')
createTab('Device 2')


## TESTCODE##########################################

def createTestTab(name):
    tab = Tab(tabControl, name)
    tabControl.addTab(tab)

    devTab = WindowPane(tab, HORIZONTAL)
    devTab.pack(fill=BOTH, expand=YES)
    devTab.config(bg='black')

    pw1 = WindowPane(devTab, VERTICAL)
    pw1.config(bg='black')

    graph = Graph(devTab)
    graph.display_graph()

    devTab.addLabel(graph)


# Create test tab
createTestTab('TEST')

#####################################################

mainFrame.mainloop()
