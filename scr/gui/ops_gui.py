
from json import JSONDecodeError
from operator import truediv
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import messagebox

from ..lib.ops import BuildOps




class AppOps(ttk.Frame):
    def __init__(self, master):
        width = 600
        height = 600
        super().__init__(master, width=width, height=height)

        self.build_ops = None

        self.textbox = font.Font(size=12)
        self.label = font.Font(size=10)

        self.pj = ttk.LabelFrame(self, text="プロジェクト")
        self.plr = ttk.LabelFrame(self, text="操作")
        self.tree = ttk.Frame(self)
        self.save = ttk.Frame(self)

        self.pj_name = ttk.Frame(self.pj)
        self.plr_name = ttk.Frame(self.plr)
        self.plr_level = ttk.Frame(self.plr)
        self.plr_bpl = ttk.Frame(self.plr)
        self.plr_add = ttk.Frame(self.plr)
        self.plr_del = ttk.Frame(self.plr)
        self.tree_viw = ttk.Frame(self.tree)
        self.save_file = ttk.Frame(self.save)

        self.pjname = tk.StringVar()
        self.plrname = tk.StringVar()
        self.plrlevel = tk.IntVar()
        self.plrbpl = tk.BooleanVar()

        self.plrlevel.set(1)
        self.plrbpl.set(False)


        self.set_pj_name()
        self.set_tree_viw()
        self.set_plr_name()
        self.set_plr_level()
        self.set_plr_bpl()
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
        self.build_ops = BuildOps()
        self.openfile_flag = True
        self.build_ops.load_whitelist(self.pjname.get())
        self.build_ops.deta_collback(self._update_tree)



    def set_plr_name(self):
        plr_namelabel = ttk.Label(self.plr_name, text="名前")
        plr_nametextbox = ttk.Entry(self.plr_name, width=30, textvariable=self.plrname)

        plr_namelabel.grid(row=0, column=0, sticky=tk.W)
        plr_nametextbox.grid(row=1, column=0, sticky=tk.W)

    def set_plr_level(self):
        plr_levellabel = ttk.Label(self.plr_level, text="level")
        plr_levelspinbox = ttk.Spinbox(self.plr_level, from_=1, to=4,textvariable=self.plrlevel)

        plr_levellabel.grid(row=0, column=0, sticky=tk.W)
        plr_levelspinbox.grid(row=1, column=0, sticky=tk.W)

    def set_plr_bpl(self):
        plr_bplcheckbox = ttk.Checkbutton(self.plr_bpl, text="最大人数を超過しての参加を許可", 
                                        variable=self.plrbpl)

        plr_bplcheckbox.pack()


    def set_plr_add(self):
        plr_addbutton = ttk.Button(self.plr_add, text="追加",command=self._addbutton)

        plr_addbutton.grid(row=1, column=1)

    def _addbutton(self):
        if not self.build_ops:
            self.build_ops = BuildOps()
        try:
            self.build_ops.deta_add(self.plrname.get(), self.plrlevel.get(), str(self.plrbpl.get()))
            self.build_ops.deta_collback(self._update_tree)
            self.plrname.set("")
            self.plrlevel.set(1)
            self.plrbpl.set(False)
        except JSONDecodeError:
            messagebox.showerror(message="プレイヤーが存在しません")

    def set_plr_del(self):
        plr_dellabel = ttk.Button(self.plr_del, text="削除", command=self._delbutton)

        plr_dellabel.grid(row=0, column=0, sticky=tk.W)

    def _delbutton(self):
        if not self.build_ops:
            self.build_ops = BuildOps()
        try:
            self.build_ops.deta_del(self.plrname.get(), self.plrlevel.get(), str(self.plrbpl.get()))
            self.build_ops.deta_collback(self._update_tree)
            self.plrname.set("")
            self.plrlevel.set(1)
            self.plrbpl.set(False)
        except JSONDecodeError:
            messagebox.showerror(message="プレイヤーが存在しません")

    def _update_tree(self,payload):
        for i in self.tree_obj.get_children():
            self.tree_obj.delete(i)

        for value in payload:
            self.tree_obj.insert("","end",value=[value["name"], value["uuid"], 
                                                value["level"], value["bypassesPlayerLimit"]])

    def _tree_viw(self,event):
        data = self.tree_obj.focus()
        data = self.tree_obj.item(data, "values")
        self.plrname.set(data[0])
        self.plrlevel.set(data[2])
        self.plrbpl.set(data[3])


    def set_tree_viw(self):
        self.tree_obj = ttk.Treeview(self.tree_viw, height=15)
        self.tree_obj.bind("<<TreeviewSelect>>", self._tree_viw)
        self.tree_obj["column"] = (1,2,3,4)
        self.tree_obj["show"] = "headings"

        self.tree_obj.heading(1,text="プレイヤー名")
        self.tree_obj.heading(2,text="uuid")
        self.tree_obj.heading(3,text="level")
        self.tree_obj.heading(4,text="BPL")
        self.tree_obj.column(1,width=190)
        self.tree_obj.column(2,width=260)
        self.tree_obj.column(3,width=45)
        self.tree_obj.column(4,width=80)
        self.tree_obj.pack()

    def set_save_file(self):
        save_filebutton = ttk.Button(self.save_file, text="保存", command=self._savebutton)

        save_filebutton.pack()

    def _savebutton(self):
        self.build_ops.create_ops(self.pjname.get())

        self.plrbpl.set(False)
        for i in self.tree_obj.get_children():
            self.tree_obj.delete(i)
        if self.build_ops.loop_count == 0:
            messagebox.showinfo(message="保存しました")
        else:
            messagebox.showinfo(message=f"同じファイル名が存在したため{self.pjname.get()}({self.build_ops.loop_count})として保存しました")
        self.pjname.set("")
        self.plrname.set("")
        self.plrlevel.set(1)
        self.build_ops = None

    def set_place(self):
        self.pj.place(x=10, y=10)
        self.pj_name.pack()
        self.plr.place(x=10, y=80)
        self.plr_name.grid(row=0, column=0, sticky=tk.W)
        self.plr_level.grid(row=1, column=0, sticky=tk.W)
        self.plr_bpl.grid(row=0, column=2, columnspan=2)
        self.plr_del.grid(row=3, column=2)
        self.plr_add.grid(row=3, column=3)
        self.tree.place(x=10, y=220)
        self.tree_viw.pack()
        self.save.place(x=480, y=180)
        self.save_file.pack()
