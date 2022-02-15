from json import JSONDecodeError
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from ..lib.whitelist import BuildWls


class AppWls(ttk.Frame):
    def __init__(self, master):
        width = 600
        height = 600
        super().__init__(master, width=width, height=height)



        self.textbox = font.Font(size=12)
        self.label = font.Font(size=10)

        self.pj = ttk.LabelFrame(self, text="プロジェクト")
        self.plr = ttk.LabelFrame(self, text="操作")
        self.tree = ttk.Frame(self)
        self.save = ttk.Frame(self)

        self.pj_name = ttk.Frame(self.pj)
        self.plr_add = ttk.Frame(self.plr)
        self.plr_del = ttk.Frame(self.plr)
        self.plr_del = ttk.Frame(self.plr)
        self.tree_viw = ttk.Frame(self.tree)
        self.save_file = ttk.Frame(self.save)

        self.pjname = tk.StringVar()
        self.plradd = tk.StringVar()
        self.plrdel = tk.StringVar()

        self.build_wls = None

        self.set_pj_name()
        self.set_tree_viw()
        self.set_plr_add()
        self.set_plr_del()
        self.set_save_file()
        self.set_place()

    def set_pj_name(self):
        pj_namelabel = ttk.Label(self.pj_name, text="ファイル名", font=self.label)
        pj_nametextbox = ttk.Entry(self.pj_name, width=30, textvariable=self.pjname, font=self.textbox)
        pj_namebutton = ttk.Button(self.pj_name, text="開く",command=self._openbutton)
        
        pj_namelabel.grid(row=0, column=0, sticky=tk.W)
        pj_nametextbox.grid(row=1,column=0)
        pj_namebutton.grid(row=1,column=1)

    def _openbutton(self):
        self.build_wls = BuildWls()
        self.openfile_flag = True
        self.build_wls.load_whitelist(self.pjname.get())
        self.build_wls.deta_collback(self._update_tree)

    def set_plr_add(self):
        plr_addlabel = ttk.Label(self.plr_add, text="追加")
        plr_addtextbox = ttk.Entry(self.plr_add, width=30, textvariable=self.plradd)
        plr_addbutton = ttk.Button(self.plr_add, text="追加",command=self._addbutton)

        plr_addlabel.grid(row=0, column=0, sticky=tk.W)
        plr_addtextbox.grid(row=1, column=0)
        plr_addbutton.grid(row=1, column=1)

    def _addbutton(self):
        if not self.build_wls:
            self.build_wls = BuildWls()
        try:
            self.build_wls.deta_add(self.plradd.get())
            self.build_wls.deta_collback(self._update_tree)
        except JSONDecodeError:
            messagebox.showerror(message="プレイヤーが存在しません")
        self.plradd.set("")

    def set_plr_del(self):
        plr_dellabel = ttk.Label(self.plr_del, text="削除")
        plr_deltextbox = ttk.Entry(self.plr_del, width=30, textvariable=self.plrdel)
        plr_delbutton = ttk.Button(self.plr_del, text="削除",command=self._delbutton)

        plr_dellabel.grid(row=0, column=0, sticky=tk.W)
        plr_deltextbox.grid(row=1, column=0)
        plr_delbutton.grid(row=1, column=1)

    def _delbutton(self):
        if not self.build_wls:
            self.build_wls = BuildWls()
        try:
            self.build_wls.deta_del(self.plrdel.get())
            self.build_wls.deta_collback(self._update_tree)
        except JSONDecodeError:
            messagebox.showerror(message="プレイヤーが存在しません")
        self.plrdel.set("")

    def _update_tree(self,payload):
        for i in self.tree_obj.get_children():
            self.tree_obj.delete(i)

        for value in payload:
            self.tree_obj.insert("","end",value=[value["name"], value["uuid"]])

    def set_tree_viw(self):
        self.tree_obj = ttk.Treeview(self.tree_viw, height=15)
        self.tree_obj["column"] = (1,2)
        self.tree_obj["show"] = "headings"

        self.tree_obj.heading(1,text="プレイヤー名")
        self.tree_obj.heading(2,text="uuid")
        self.tree_obj.column(2,width=350)
        self.tree_obj.pack()

    def set_save_file(self):
        save_filebutton = ttk.Button(self.save_file, text="保存", command=self._savebutton)

        save_filebutton.pack()

    def _savebutton(self):
        self.build_wls.create_wls(file_name=self.pjname.get())
        for i in self.tree_obj.get_children():
            self.tree_obj.delete(i)
        if self.build_wls.loop_count == 0:
            messagebox.showinfo(message="保存しました")
        else:
            messagebox.showinfo(message=f"同じファイル名が存在したため{self.pjname.get()}({self.build_wls.loop_count})として保存しました")
        self.plradd.set("")
        self.plrdel.set("")
        self.pjname.set("")
        self.build_wls = None

    def set_place(self):
        self.pj.place(x=10, y=10)
        self.pj_name.pack()
        self.plr.place(x=10, y=80)
        self.plr_add.pack()
        self.plr_del.pack()
        self.tree.place(x=20, y=220)
        self.tree_viw.pack()
        self.save.place(x=480, y=180)
        self.save_file.pack()
