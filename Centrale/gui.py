from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import connect
import threading


class MainFrame(Tk):
    devices = []

    def __init__(self):
        super().__init__()
        self.title('Central Control Unit')
        self.geometry('750x750')

    def addDevices(self, devices):
        self.devices = devices

        self.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        for device in self.devices:
            device.stop()

        self.destroy()


class WindowPane(PanedWindow):

    def __init__(self, parent, orient):
        super().__init__(parent, orient=orient)

    def addLabels(self, *labels, height):
        # placeholder
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

    # def drawLine(self, x1, y1, x2, y2, arg=''):
    #    self.canvas.create_line(x1, y1, x2, y2, fill=arg)


class TabControl(ttk.Notebook):

    def __init__(self, mainframe):
        super().__init__(mainframe)

    def addTabs(self, *tabs):
        # placeholder
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

    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        # self.config(height=50, width=50)


class MyEntry(Entry):

    def __init__(self, parent, text):
        super().__init__(parent)
        self.insert(0, text)


class Main:
    def __init__(self, device, tabControl):
        self.device = device
        self.tempx2 = 40
        self.lightx2 = 40

        self.lighty2 = self.yValueLight(0)
        self.tempy2 = self.yValueTemp(0)

        self.tempAxis = 1
        self.lightAxis = 1

        # Entry values (met default)
        self.Afstand = 100
        self.MinTemperatuur = 10
        self.MaxTemperatuur = 20
        self.MinLicht = 10
        self.MaxLicht = 20

        # automode off/on 0/1
        self.automode = 0

        # uitrolLengte  (0/1/2/3/4/5)  wordt vermenigvuldigd met 20)
        self.uitrolLengte = 0

        # graph verplaatst vanuit createTab()
        self.graph1 = Canvas(width=350, height=250, background="gray94")
        self.graph2 = Canvas(width=350, height=250, background="gray94")

        # Image
        self.imageCanvas = Canvas(width=350, height=250, background="gray94")
        self.setImage(self.uitrolLengte)

        self.name = device.name

        self.createTab(tabControl)

    def createTab(self, tabControl):
        self.tab = Tab(tabControl, self.name)
        tabControl.addTab(self.tab)

        devTab = WindowPane(self.tab, HORIZONTAL)
        devTab.grid(row=0, column=1)

        pw1 = WindowPane(devTab, VERTICAL)
        pw2 = WindowPane(devTab, VERTICAL)

        placeholder1 = WindowPane(pw1, HORIZONTAL)
        placeholder2 = WindowPane(pw2, HORIZONTAL)
        placeholder3 = WindowPane(pw2, HORIZONTAL)

        afstandLabel = MyLabel(pw1, "Lengte")
        instellingenLabel = MyLabel(pw1, "Instellingen")
        temperatuurLabel = MyLabel(pw2, "Temperatuur")
        lichtLabel = MyLabel(pw2, "Licht")

        entryLabelAfstand = MyLabel(pw1, "Afstand:   (cm)")
        entryLabelMinTemperatuur = MyLabel(pw1, "Min Temperatuur:   (\N{DEGREE SIGN}C)")
        entryLabelMaxTemperatuur = MyLabel(pw1, "Max Temperatuur:   (\N{DEGREE SIGN}C)")
        entryLabelMinLicht = MyLabel(pw1, "Min Lichtintensiteit:")
        entryLabelMaxLicht = MyLabel(pw1, "Max Lichtintensiteit:")

        self.entryAfstand = MyEntry(pw1, self.Afstand)
        self.entryMinTemperatuur = MyEntry(pw1, self.MinTemperatuur)
        self.entryMaxTemperatuur = MyEntry(pw1, self.MaxTemperatuur)
        self.entryMinLicht = MyEntry(pw1, self.MinLicht)
        self.entryMaxLicht = MyEntry(pw1, self.MaxLicht)

        automodeBox = Checkbutton(pw1, text='auto-mode (checked = on)'
                                            '                                                        '
                                            , command=self.setAutomode)

        emptylabel = MyLabel(pw2, "")
        emptylabel2 = MyLabel(placeholder1, "")
        emptylabel3 = MyLabel(pw2, "")
        emptylabel4 = MyLabel(pw2, "")

        devTab.addLabels(pw1, pw2, height=0)

        #Settings button
        btn = MyButton(placeholder1, 'Instellen', self.setSettings)
        self.btnUp = MyButton(placeholder1, 'Omhoog', self.decrState)
        self.btnDown = MyButton(placeholder1, 'Omlaag', self.incrState)


        pw1.addLabels(afstandLabel, self.imageCanvas, instellingenLabel, automodeBox,
                      entryLabelAfstand, self.entryAfstand,
                      entryLabelMinTemperatuur, self.entryMinTemperatuur,
                      entryLabelMaxTemperatuur, self.entryMaxTemperatuur,
                      entryLabelMinLicht, self.entryMinLicht,
                      entryLabelMaxLicht, self.entryMaxLicht,
                      height=0)
        pw1.addLabel(placeholder1, 30, 100)
        placeholder1.addLabel(btn, 50, 100)
        placeholder1.addLabel(emptylabel2, 30, 50)
        placeholder1.addLabel(self.btnUp, 50, 110)
        placeholder1.addLabel(self.btnDown, 50, 50)

        pw2.addLabels(temperatuurLabel, height=0)
        pw2.addLabel(placeholder2, 0, 10)
        placeholder2.addLabel(self.graph1, 250, 350)
        placeholder2.addLabel(emptylabel3, 30, 0)
        # pw2.addLabel(graph1, 0, 0)
        # pw1.grid(row=0, column=0)
        # pw2.grid(row=0, column=1, padx=(10, 10))

        self.graphInit(self.graph1, 30, 10)
        self.graphInit(self.graph2, 0, 40)

        pw2.addLabels(lichtLabel, height=0)
        pw2.addLabel(placeholder3, 250, 10)
        placeholder3.addLabel(self.graph2, 250, 350)
        placeholder3.addLabel(emptylabel4, 30, 0)

        pw2.addLabel(emptylabel, 20, 100)

        return tabControl


    def setAutomode(self):
        if self.automode == 1:
            self.automode = 0
            self.btnUp.config(state='active')
            self.btnDown.config(state='active')
            self.device.data_to_send(3)
        else:
            self.automode = 1
            self.btnUp.config(state='disabled')
            self.btnDown.config(state='disabled')
            self.device.data_to_send(4)

    def incrState(self):
        if self.uitrolLengte < 5 and self.automode == 0:
            self.uitrolLengte = self.uitrolLengte + 1
            self.setImage(self.uitrolLengte * 20)

    def decrState(self):
        if self.uitrolLengte > 0 and self.automode == 0:
            self.uitrolLengte = self.uitrolLengte - 1
            self.setImage(self.uitrolLengte * 20)

    def setImage(self, filename):
        self.filename = ImageTk.PhotoImage(Image.open("afbeeldingen/zonnescherm" + str(filename) + ".png"))
        self.imageCanvas.image = self.filename
        self.imageCanvas.create_image(25, 2, anchor=NW, image=self.filename)

    def setSettings(self):
        self.Afstand = self.entryAfstand.get()
        self.MinTemperatuur = self.entryMinTemperatuur.get()
        self.MaxTemperatuur = self.entryMaxTemperatuur.get()
        self.MinLicht = self.entryMinLicht.get()
        self.MaxLicht = self.entryMaxLicht.get()

    def yValueTemp(self, value):
        if value >= 0:
            return 220 - 75 - value * 2.5
        else:
            value = 30 - abs(value)
            return 220 - value * 2.5

    def yValueLight(self, value):
            return 220 - value * 0.625

    def drawTemperature(self, y):
        if (self.tempAxis == 13):
            self.tempAxis = 1
            self.graph1.delete("temp")
            self.tempx2 = 40
        self.tempx1 = self.tempx2
        self.tempy1 = self.tempy2
        self.tempx2 = 40 + 25 * self.tempAxis
        self.tempy2 = self.yValueTemp(y)
        self.graph1.create_line(self.tempx1, self.tempy1, self.tempx2, self.tempy2, fill="blue", tags="temp")
        self.tempAxis = self.tempAxis + 1

    def drawLight(self, y):
        if (self.lightAxis == 13):
            self.lightAxis = 1
            self.graph2.delete("temp")
            self.lightx2 = 40
        self.lightx1 = self.lightx2
        self.lighty1 = self.lighty2
        self.lightx2 = 40 + 25 * self.lightAxis
        self.lighty2 = self.yValueLight(y)
        self.graph2.create_line(self.lightx1, self.lighty1, self.lightx2, self.lighty2, fill="blue", tags="temp")
        self.lightAxis = self.lightAxis + 1

    def graphInit(self, graph, negative, stepcount):

        for i in range(13):
            x = 40 + (i * 25)
            graph.create_line(x, 220, x, 20, width=1, dash=(2, 5))
            graph.create_text(x, 220, text='%d' % (i), anchor=N)
        for i in range(9):
            y = 220 - (i * 25)
            graph.create_line(40, y, 340, y, width=1, dash=(2, 5))
            graph.create_text(30, y, text='%d' % (stepcount * i - negative), anchor=E)


mainFrame = MainFrame()
tabControl = TabControl(mainFrame)
tabControl.grid(row=0)

# main1 = Main("Device 1", tabControl)
# main2 = Main("Device 2", tabControl)
#
# main1.drawLight(280)
# main1.drawLight(320)
# main1.drawLight(30)
# main1.drawLight(40)
# main1.drawLight(10)
# main1.drawLight(20)
# main1.drawLight(80)
# main1.drawLight(60)
# main1.drawLight(70)
# main1.drawLight(50)
# main1.drawLight(30)
# main1.drawLight(60)
#
# main1.drawTemperature(-11)
# main1.drawTemperature(32)
# main1.drawTemperature(45)
# main1.drawTemperature(17)
# main1.drawTemperature(29)
# main1.drawTemperature(-5)
# main1.drawTemperature(-11)
# main1.drawTemperature(-25)
# main1.drawTemperature(-30)
# main1.drawTemperature(31)
# main1.drawTemperature(1)
# main1.drawTemperature(17)

#mainFrame.mainloop()