from tkinter import *
from tkinter import ttk


class MainFrame(Tk):

    def __init__(self):
        super().__init__()
        self.title('Central Control Unit')
        self.geometry('750x750')


class WindowPane(PanedWindow):

    def __init__(self, parent, orient):
        super().__init__(parent, orient=orient)

    def addLabels(self, *labels, height):
        #placeholder
        for label in labels:
            self.add(label, stretch="always", height=height, width=375)

    def addLabel(self, label, height):
        self.add(label, height=height, width=100)


class Graph(WindowPane):

    def __init__(self, parent):
        super().__init__(parent, orient=HORIZONTAL)
        pass


class MyCanvas(Canvas):

    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = Canvas(self, width=1200, height=600, background="white")
        self.canvas.create_line(0, 0, 200, 100)
        self.canvas.create_line(0, 100, 200, 0, fill='red')


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





class MyLabel(Label):

    def __init__(self, parent, text):
        super().__init__(parent, text=text, anchor=NW)


class MyButton(Button):

    def __init__(self, parent, text):
        super().__init__(parent, text=text)
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
    devTab.grid(row=0, column=1)
    pw1 = WindowPane(devTab, VERTICAL)
    pw2 = WindowPane(devTab, VERTICAL)
    pw3 = WindowPane(pw1, HORIZONTAL)

    afstandLabel = MyLabel(pw1, "AFSTANDAFBEELDING 1")
    instellingenLabel = MyLabel(pw1, "Instelling 1")
    temperatuurLabel = MyLabel(pw2, "Temperatuur 1")
    lichtLabel = MyLabel(pw2, "Licht 1")

    emptylabel = MyLabel(pw2, "")
    emptylabel2 = MyLabel(pw3, "")

    devTab.addLabels(pw1, pw2, height=0)
    btn = MyButton(pw3, name)

    pw1.addLabels(afstandLabel, instellingenLabel, height=345)
    pw2.addLabels(temperatuurLabel, lichtLabel, height=250)

    pw1.addLabel(pw3, 30)
    pw3.addLabel(btn, 50)
    pw3.addLabel(emptylabel2, 30)
    pw2.addLabel(emptylabel, 20)


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
    canvas = MyCanvas(graph)
    graph.addLabel(canvas, 500)

    devTab.addLabel(graph, 500)



# Create test tab
createTestTab('TEST')

#####################################################

mainFrame.mainloop()
