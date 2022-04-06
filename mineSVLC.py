
from shutil import rmtree
from scr.gui.main_gui import AppMain
import tkinter as tk
import scr.lib.setups as setup

###build用インポート###
import email
import http
import http.client
####################

if __name__ == '__main__':
    try:
        rmtree("./server/temp")
    except FileNotFoundError:
        pass

    setup.setup()

    root = tk.Tk()
    gui = AppMain(master=root)
    gui.rowconfigure(0, weight=1)
    gui.columnconfigure(0, weight=1)
    gui.mainloop()

