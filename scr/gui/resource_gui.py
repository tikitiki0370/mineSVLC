from tkinter import ttk

class AppRes(ttk.Frame):
    def __init__(self,master):
        width = 600
        height = 600
        super().__init__(master, width=width, height=height)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def set_default_value(self):
        pass