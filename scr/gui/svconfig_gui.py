import json
import tkinter as tk
from tkinter import font, messagebox, ttk

from ..lib.server_properties import build_svpr, load_file


class AppSvc(ttk.Frame):
    def __init__(self, master):
        width = 600
        height = 600
        super().__init__(master, width=width, height=height)

        self.openfile_flag = False

        self.textbox = font.Font(size=12)
        self.label = font.Font(size=10)

        self.pj = ttk.LabelFrame(self, text="プロジェクト")
        self.setting = ttk.LabelFrame(self, text="操作")
        self.save = ttk.Frame(self)


        self.pj_name = ttk.Frame(self.pj)
        self.cnf_ls = ttk.Frame(self.setting)
        self.cnf_pnl = ttk.Frame(self.setting)
        self.save_file = ttk.Frame(self.save)


        self.pjname = tk.StringVar()
        self.cnfname = tk.StringVar()

        self.cnfname.set("選択してください")

        self.__build_objls()


        self.set_pj_name()
        self.set_cnf_ls()
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
        try:
            load_file(self.pjname.get(), self._var_sets)
        except:
            messagebox.showerror("エラー", "ファイルを読み込めませんでした")
            return
        messagebox.showinfo("", "ファイルを読み込みました")

    def _var_sets(self, payload):
        for i in payload:
            self.vlr_dict[i].set(payload[i])

    def set_cnf_ls(self):
        setting_cnflabel = ttk.Label(self.cnf_ls, text="設定")
        setting_cnfpulldown = ttk.Combobox(self.cnf_ls, values=self.cnf_pulldown_vlr, textvariable=self.cnfname, state="readonly")

        setting_cnfpulldown.bind('<<ComboboxSelected>>', self._update_cnf_ls)
        setting_cnflabel.grid(row=0, column=0, sticky=tk.W)
        setting_cnfpulldown.grid(row=1, column=0, sticky=tk.W)

    def _update_cnf_ls(self, event=None):
        if self.cnfname.get() == "サーバー設定": self.set_cnf_sv()
        elif self.cnfname.get() == "接続設定": self.set_cnf_connection()
        elif self.cnfname.get() == "ゲーム設定": self.set_cnf_game()
        elif self.cnfname.get() == "スポーン設定": self.set_cnf_spawn()
        elif self.cnfname.get() == "通信設定": self.set_cnf_conect()
        elif self.cnfname.get() == "ワールド生成": self.set_cnf_world()
        elif self.cnfname.get() == "外部通信": self.set_cnf_out()
        elif self.cnfname.get() == "権限": self.set_cnf_ops()
        elif self.cnfname.get() == "認証": self.set_cnf_auth()
        else:
            for i in self.cnf_pnl.winfo_children():
                i.destroy()
            self._set_build_obj(self.cnfname.get())

    def set_cnf_sv(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("level-name","motd","max-players", "max-tick-time", "enable-command-block", "pvp")

    def set_cnf_connection(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("server-port","server-ip","resource-pack", "resource-pack-sha1", "require-resource-pack", "resource-pack-prompt")

    def set_cnf_game(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("gamemode","force-gamemode","difficulty", "hardcore", "max-world-size", "max-build-height")

    def set_cnf_spawn(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("spawn-protection", "spawn-npcs", "spawn-monstar", "spawn-animals")

    def set_cnf_conect(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("network-compression-threshold", "view-distance", "snooper-enabled", 
                            "entity-broadcast-range-percentage", "use-native-transport", "rate-limit")

    def set_cnf_world(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("level-type", "level-seed", "generator-settings", "generate-structures")

    def set_cnf_out(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("rcon.port", "rcon.password", "broadcast-rcon-to-ops", "enable-query",
                            "query.port", "enable-jmx-monitoring")

    def set_cnf_ops(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("op-permission-level", "function-permission-level", "allow-nether", "allow-flight",
                            "broadcast-console-to-ops")

    def set_cnf_auth(self):
        for i in self.cnf_pnl.winfo_children():
            i.destroy()
        self._set_build_obj("whitelist", "enforce-whitelist", "online-mode", "prevent-proxy-connections",
                            "player-idle-timeout")

    def set_save_file(self):
        save_filebutton = ttk.Button(self.save_file, text="保存", command=self._savebutton)

        save_filebutton.pack()

    def _savebutton(self):
        payload = {}
        for i in self.vlr_dict:
            payload[i] = self.vlr_dict[i].get()
        roop_count = build_svpr(self.pjname.get(), payload)
        if roop_count == 0:
            messagebox.showinfo("", "作成しました")
        else:
            messagebox.showinfo("", f"同じ名前が存在したため{self.pjname.get()}({roop_count})として作成しました")
        self.__build_objls()
        self._update_cnf_ls()

    def set_place(self):
        self.pj.place(x=10, y=10)
        self.pj_name.pack()
        self.setting.place(x=10,y=80)
        self.cnf_ls.grid(row=0, column=0, sticky=tk.W)
        self.cnf_pnl.grid(row=1, column=0, sticky=tk.W)
        self.save.place(x=500,y=230)
        self.save_file.grid(row=0, column=0)

    def _set_build_obj(self, *arg):
        for i, j in enumerate(arg):
            #テキストボックス用
            if j in self.gui_data["str_obj"].keys():
                label = ttk.Label(self.cnf_pnl, **self.gui_data["str_obj"][j][0])
                entry = ttk.Entry(self.cnf_pnl, **self.gui_data["str_obj"][j][1])
                if 0 == i%2:
                    label.grid(row=i, column=0, sticky=tk.W)
                    entry.grid(row=i+1, column=0, sticky=tk.W)
                else:
                    label.grid(row=i-1, column=1, sticky=tk.W, padx=10)
                    entry.grid(row=i, column=1, sticky=tk.W, padx=10)
            #スピンボックス用
            elif j in self.gui_data["int_obj"].keys():
                label = ttk.Label(self.cnf_pnl, **self.gui_data["int_obj"][j][0])
                spinbox = ttk.Spinbox(self.cnf_pnl, **self.gui_data["int_obj"][j][1])
                if 0 == i%2:
                    label.grid(row=i, column=0, sticky=tk.W)
                    spinbox.grid(row=i+1, column=0, sticky=tk.W)
                else:
                    label.grid(row=i-1, column=1, sticky=tk.W, padx=10)
                    spinbox.grid(row=i, column=1, sticky=tk.W, padx=10)
            #チェックボックス用
            elif j in self.gui_data["bool_obj"].keys():
                label = ttk.Label(self.cnf_pnl, **self.gui_data["bool_obj"][j][0])
                checkbox = ttk.Checkbutton(self.cnf_pnl, **self.gui_data["bool_obj"][j][1])
                if 0 == i%2:
                    label.grid(row=i, column=0, sticky=tk.W)
                    checkbox.grid(row=i+1, column=0, sticky=tk.W)
                else:
                    label.grid(row=i-1, column=1, sticky=tk.W, padx=10)
                    checkbox.grid(row=i, column=1, sticky=tk.W, padx=10)

    def __build_objls(self):
        self.cnf_pulldown_vlr = ["サーバー設定", "接続設定", "ゲーム設定", "スポーン設定", "通信設定", 
                                "ワールド生成", "外部通信", "権限", "認証"]

        self.vlr_dict = {}


        with open("./data/config/svcnfdata.json", "r") as f:
            self.gui_data = json.load(f)

        for i in self.gui_data:
            for j in self.gui_data[i]:
                if "textvariable" in self.gui_data[i][j][1].keys():
                    var_type = "textvariable"
                elif "variable" in self.gui_data[i][j][1].keys():
                    var_type = "variable"

                payload = self.gui_data[i][j][1][var_type]
                if i == "str_obj":
                    self.vlr_dict[payload[0]] = tk.StringVar()
                elif i == "int_obj":
                    self.vlr_dict[payload[0]] = tk.IntVar()
                elif i == "bool_obj":
                    self.vlr_dict[payload[0]] = tk.BooleanVar()
                else:
                    raise KeyError
                self.vlr_dict[payload[0]].set(payload[1])
                self.gui_data[i][j][1][var_type] = self.vlr_dict[payload[0]]
                self.cnf_pulldown_vlr.append(j)
