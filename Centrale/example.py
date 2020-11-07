from tkinter import *
from tkinter import ttk

frame = ttk.Frame()
l1 = Label(frame)
l2 = Label(frame)
l1.grid(row=0, column=0, sticky="nsew")
l2.grid(row=1, column=1, sticky="nsew")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

frame.mainloop()