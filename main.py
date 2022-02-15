
from shutil import rmtree
from scr.gui.main_gui import AppMain
import tkinter as tk



if __name__ == '__main__':
    try:
        rmtree("./server/temp")
    except FileNotFoundError:
        pass
    root = tk.Tk()
    gui = AppMain(master=root)
    gui.rowconfigure(0, weight=1)
    gui.columnconfigure(0, weight=1)

    gui.mainloop()

