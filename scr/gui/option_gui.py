from tkinter import ttk

class OptionsGui(ttk.Frame):
    def __init__(self,master) -> None:
        width = 300
        height = 300
        super().__init__(master,width=width, height=height)
        