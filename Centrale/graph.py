from tkinter import *
from tkinter import ttk


class Graph(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = Canvas(self, width=1200, height=600, background="white")
        self.canvas.create_line(0, 0, 200, 100)
        self.canvas.create_line(0, 100, 200, 0, fill='red')

        

        #voor MyCanvas
        #self.canvas = MyCanvas(self, 200, 600, "white")

    #def display_graph(self):



# class MyCanvas(Canvas):
#     def __init__(self, parent, width, heigth, bg):
#         super().__init__(parent, width=width, heigth=heigth, background=bg)
#
