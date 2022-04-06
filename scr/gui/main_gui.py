from tkinter import Menu, ttk
import tkinter as tk

from scr.gui.home_gui import AppHome
from scr.gui.ops_gui import AppOps
from scr.gui.resource_gui import AppRes
from scr.gui.svconfig_gui import AppSvc
from scr.gui.whitelist_gui import AppWls


class AppMain(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.master.geometry("600x600")
        self.master.title("mineSVLC")

        self.set_menu()
        self.set_note()

    def set_menu(self):
        menuber = Menu(self.master)
        #fileメニュー設定
        filemenu = Menu(menuber, tearoff=0)
        filemenu.add_command(label="終了",command=self.master.quit)

        #配置
        menuber.add_cascade(label="ファイル", menu=filemenu)
        self.master.config(menu=menuber)

    def set_option(self):
        
        tk.Toplevel(self.master, )
        pass

    def set_note(self):
        note = ttk.Notebook(self.master)
        note.pack()
        self.home = AppHome(note)
        self.svc = AppSvc(note)
        self.res = AppRes(note)
        self.wls = AppWls(note)
        self.ops = AppOps(note)
        note.add(self.home,text="サーバー")
        note.add(self.svc,text="プロパティ")
        note.add(self.wls,text="ホワイトリスト")
        note.add(self.ops,text="OPリスト")
