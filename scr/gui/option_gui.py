
from tkinter import ttk
import tkinter as tk

class OptionsGui(ttk.Frame):
    def __init__(self,master) -> None:
        
        width = 600
        height = 600
        super().__init__(master,width=width, height=height)

if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("600x600")
    gui = OptionsGui(master=root)
    gui.mainloop()