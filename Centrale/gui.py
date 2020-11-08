from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


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

    def addLabel(self, label, height, width):
        self.add(label, height=height, width=width)


class Graph(Canvas):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=1200, height=600, background="white")
        self.draw_axes()
        self.draw_roster()

    def draw_axes(self):
        # X-axis
        self.canvas.create_line(0, 0, 500, 0)
        # Y-axis
        self.canvas.create_line(0, 0, 0, 500)

    def draw_roster(self):
        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            self.canvas.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.canvas.create_text(x, 550, text='%d' % (10 * i), anchor=N)
        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)

    #def drawLine(self, x1, y1, x2, y2, arg=''):
    #    self.canvas.create_line(x1, y1, x2, y2, fill=arg)


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

mainFrame = MainFrame()
tabControl = TabControl(mainFrame)
tabControl.grid(row=0)


class Main:
    def __init__(self, name):
        self.x2 = 40
        self.y2 = self.yValue(0)
        self.s = 1

        self.graph1 = Canvas(width=350, height=250, background="white")
        self.graph2 = Canvas(width=350, height=250, background="white")
        self.imageCanvas = Canvas(width=350, height=250, background="black")

        self.setImage('zonnescherm80.png')

        self.createTab(name)

    def createTab(self, name):
        self.tab = Tab(tabControl, name)
        tabControl.addTab(self.tab)

        devTab = WindowPane(self.tab, HORIZONTAL)
        devTab.grid(row=0, column=1)

        pw1 = WindowPane(devTab, VERTICAL)
        pw2 = WindowPane(devTab, VERTICAL)

        placeholder1 = WindowPane(pw1, HORIZONTAL)
        placeholder2 = WindowPane(pw2, HORIZONTAL)
        placeholder3 = WindowPane(pw2, HORIZONTAL)

        self.imageCanvas.image = self.filename
        self.imageCanvas.create_image(0, 0, anchor=NW, image=self.filename)


        afstandLabel = MyLabel(pw1, "AFSTANDAFBEELDING 1")
        instellingenLabel = MyLabel(pw1, "Instelling 1")
        temperatuurLabel = MyLabel(pw2, "Temperatuur 1")
        lichtLabel = MyLabel(pw2, "Licht 1")

        emptylabel = MyLabel(pw2, "")
        emptylabel2 = MyLabel(placeholder1, "")
        emptylabel3 = MyLabel(pw2, "")
        emptylabel4 = MyLabel(pw2, "")

        devTab.addLabels(pw1, pw2, height=0)
        btn = MyButton(placeholder1, name)

        pw1.addLabels(afstandLabel, self.imageCanvas, instellingenLabel, height=0)
        pw1.addLabel(placeholder1, 30, 100)
        placeholder1.addLabel(btn, 50, 100)
        placeholder1.addLabel(emptylabel2, 30, 100)
        
        pw2.addLabels(temperatuurLabel, height=0)
        pw2.addLabel(placeholder2, 0, 10)
        placeholder2.addLabel(self.graph1, 250, 350)
        placeholder2.addLabel(emptylabel3, 30, 0)
        #pw2.addLabel(graph1, 0, 0)
        #pw1.grid(row=0, column=0)
        #pw2.grid(row=0, column=1, padx=(10, 10))    

        self.graphInit(self.graph1)
        self.graphInit(self.graph2)

        pw2.addLabels(lichtLabel, height=0)
        pw2.addLabel(placeholder3, 250, 10)
        placeholder3.addLabel(self.graph2, 250, 350)
        placeholder3.addLabel(emptylabel4, 30, 0)

        
        
        pw2.addLabel(emptylabel, 20, 100)

    def setImage(self, filename):
        self.filename = ImageTk.PhotoImage(Image.open("afbeeldingen/"+filename))

    def yValue(self, value):
        return 220 - value * 2.5

    def drawLine(self, y):
        self.x1 = self.x2
        self.y1 = self.y2
        self.x2 = 40 + 25 * self.s
        self.y2 = self.yValue(y)
        self.graph1.create_line(self.x1, self.y1, self.x2, self.y2, fill="blue")
        self.graph2.create_line(self.x1, self.y1, self.x2, self.y2, fill="blue")
        self.s = self.s + 1
    
    def graphInit(self, graph):
        for i in range(13):
            x = 40 + (i * 25)
            graph.create_line(x,220,x,20, width=1, dash=(2,5))
            graph.create_text(x,220, text='%d'% (10*i), anchor=N)
        for i in range(9):
            y = 220 - (i * 25)
            graph.create_line(40,y,340,y, width=1, dash=(2,5))
            graph.create_text(30,y, text='%d'% (10*i), anchor=E)


main1 = Main("Device 1")
main2 = Main("Device 2")

main1.drawLine(70)
main1.drawLine(50)
main1.drawLine(30)
main1.drawLine(40)
main1.drawLine(10)
main1.drawLine(20)
main1.drawLine(80)
main1.drawLine(60)


mainFrame.mainloop()

