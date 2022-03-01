import asyncio
import tkinter as tk
from glob import glob
from tkinter import filedialog, font, messagebox, ttk

from ..lib.build_sv import BuildSV
from ..lib.manifest_parser import parser


class AppHome(ttk.Frame):
    def __init__(self, master):
        width = 600
        height = 600
        super().__init__(master, width=width, height=height)
        self.textbox = font.Font(size=12)
        self.label = font.Font(size=10)
        self.pj = ttk.LabelFrame(self, text="プロジェクト")
        self.sv = ttk.LabelFrame(self, text="サーバー設定")
        self.st = ttk.LabelFrame(self, text="起動設定")
        self.buildsv = ttk.Frame(self)

        self.pj_name = ttk.Frame(self.pj)
        self.sv_ver = ttk.Frame(self.sv)
        self.sv_cnf = ttk.Frame(self.sv)
        self.sv_mem = ttk.Frame(self.sv)
        self.sv_jarg = ttk.Frame(self.sv)
        self.sv_world = ttk.Frame(self.sv)
        self.sv_ops = ttk.Frame(self.sv)
        self.sv_white = ttk.Frame(self.sv)
        self.st_sets = ttk.Frame(self.st)

        self.svcsnap = tk.BooleanVar()
        self.svver = tk.StringVar()
        self.svcnf = tk.StringVar()
        self.pjname = tk.StringVar()
        self.jvmarg = tk.StringVar()
        self.svmemmin = tk.IntVar()
        self.svmemmax = tk.IntVar()
        self.worldpath =tk.StringVar()
        self.ops = tk.StringVar()
        self.whitelist = tk.StringVar()
        self.progles = tk.IntVar()


        self.svver.set("選択してください")
        self.svmemmin.set(1024)
        self.svmemmax.set(1024)

        self.set_pj_name()
        self.set_sv_ver()
        self.set_sv_cnf()
        self.set_sv_mem()
        self.set_sv_jarg()
        self.set_sv_world()
        self.set_sv_ops()
        self.set_sv_white()
        self.set_st_stsets()
        self.set_buildst_button()
        self.set_place()
        self.load_verls()


    def update_verls(self):
        if self.svcsnap.get():
            self.sv_vertextbox["values"] = self.ver_release
        else:
            self.sv_vertextbox["values"] = self.ver_snapshot
    def load_verls(self):
        try:
            ver_release, ver_snapshot, build_url = parser()
        except FileNotFoundError:
            messagebox.showerror("ファイルが存在しません","マインクラフトランチャーが必要です")
        self.ver_release = ver_release
        self.ver_snapshot = ver_snapshot
        self.build_url = build_url

    def open_filewindow(self):
        self.worldpath.set(filedialog.askdirectory(initialdir="./"))


    def set_pj_name(self):
        pj_namelabel = ttk.Label(self.pj_name, text="ファイル名", font=self.label)
        pj_nametextbox = ttk.Entry(self.pj_name, width=30, textvariable=self.pjname, font=self.textbox)
        
        pj_namelabel.grid(row=0, column=0, sticky=tk.W)
        pj_nametextbox.grid(row=1,column=0)

    def set_sv_ver(self):
        sv_verlabel = ttk.Label(self.sv_ver, text="バージョン", font=self.label)
        self.sv_vertextbox = ttk.Combobox(self.sv_ver, width=20, values="選択してください",
                                    textvariable=self.svver, postcommand=self.update_verls)
        sv_vercheckbox = ttk.Checkbutton(self.sv_ver, text="スナップショットを表示", variable=self.svcsnap)

        sv_verlabel.grid(row=0, column=0, sticky=tk.W)
        self.sv_vertextbox.grid(row=1, column=0, sticky=tk.W)
        sv_vercheckbox.grid(row=1, column=1, padx=10, sticky=tk.W)

    def set_sv_cnf(self):
        sv_cnflabel = ttk.Label(self.sv_cnf, text="サーバープロパティ", font=self.label)
        self.sv_cnftextbox = ttk.Combobox(self.sv_cnf,width=25, textvariable=self.svcnf, postcommand=self._update_cnf)

        sv_cnflabel.grid(row=0, column=0, sticky=tk.W)
        self.sv_cnftextbox.grid(row=1, column=0)

    def _update_cnf(self):
        value = [i[21:i.index(".", 21)] for i in glob("./data/sv_properties/*.properties")]
        self.sv_cnftextbox["values"] = value

    def set_sv_mem(self):
        sv_memlabel = ttk.Label(self.sv_mem, text="メモリ", font=self.label)
        sv_mem_minmax = ttk.Label(self.sv_mem, text="～")
        sv_memspinbox_min = ttk.Spinbox(self.sv_mem, from_=512, to=20480, increment=512,
                                textvariable=self.svmemmin, width=8, font=self.textbox)
        sv_memspinbox_max = ttk.Spinbox(self.sv_mem, from_=512, to=20480, increment=512,
                                textvariable=self.svmemmax, width=8, font=self.textbox)
        
        sv_memlabel.grid(row=0, column=0, sticky=tk.W)
        sv_memspinbox_min.grid(row=1, column=0)
        sv_mem_minmax.grid(row=1, column=1)
        sv_memspinbox_max.grid(row=1, column=2)

    def set_sv_world(self):
        sv_worldlabel = ttk.Label(self.sv_world, text="ワールドファイル")
        sv_worldtextbox = ttk.Entry(self.sv_world, width=40, textvariable=self.worldpath)
        sv_worldbutton = ttk.Button(self.sv_world, width=5, text="開く", command=self.open_filewindow)

        sv_worldlabel.grid(row=0, column=0, sticky=tk.W)
        sv_worldtextbox.grid(row=1, column=0)
        sv_worldbutton.grid(row=1, column=1)

    def set_sv_jarg(self):
        sv_jarglabel = ttk.Label(self.sv_jarg, text="jvm引数")
        sv_jargtextbox = ttk.Entry(self.sv_jarg, width=35, textvariable=self.jvmarg, font=self.textbox, state=tk.DISABLED)

        sv_jarglabel.grid(row=0, column=0, sticky=tk.W)
        sv_jargtextbox.grid(row=1, column=0)

    def set_sv_ops(self):
        sv_opslabel = ttk.Label(self.sv_ops, text="ops")
        self.sv_opspulldown = ttk.Combobox(self.sv_ops, textvariable=self.ops, postcommand=self._update_ops)

        sv_opslabel.grid(row=0, column=0, sticky=tk.W)
        self.sv_opspulldown.grid(row=1, column=0)

    def _update_ops(self):
        value = [i[11:i.index(".", 11)] for i in glob("./data/ops/*.json")]
        self.sv_opspulldown["values"] = value

    def set_sv_white(self):
        sv_whitelabel = ttk.Label(self.sv_white, text="whitelist")
        self.sv_whitepulldown = ttk.Combobox(self.sv_white, textvariable=self.whitelist, postcommand=self._update_white)

        sv_whitelabel.grid(row=0, column=0, sticky=tk.W)
        self.sv_whitepulldown.grid(row=1, column=0)

    def _update_white(self):
        value = [i[17:i.index(".", 17)] for i in glob("./data/whitelist/*.json")]
        self.sv_whitepulldown["values"] = value

    def set_st_stsets(self):
        st_stsetslabel_bef = ttk.Label(self.st_sets, text="起動前に行う処理")
        st_stsetslabel_aft = ttk.Label(self.st_sets, text="終了時に行う処理")
        self.st_stsetstext_bef = tk.Text(self.st_sets, width=71, height=6)
        self.st_stsetstext_aft = tk.Text(self.st_sets, width=71, height=6)

        self.st_stsetstext_bef.configure(font=self.textbox)
        self.st_stsetstext_aft.configure(font=self.textbox)

        st_stsetslabel_bef.grid(row=0, column=0, sticky=tk.W)
        self.st_stsetstext_bef.grid(row=1, column=0)
        st_stsetslabel_aft.grid(row=2, column=0, sticky=tk.W)
        self.st_stsetstext_aft.grid(row=3, column=0)

    def set_buildst_button(self):
        self.build_buildbutton = ttk.Button(self.buildsv, text="作成", command=self._buildbutton)

        self.build_buildbutton.grid(row=0, column=0)

    def _buildbutton(self):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self._build_sv)

    def _printsarg(self, block_count, block_size, file_size):
        #collback build_sv -> THIS
        if not self.popup_flag:
            self._popup_progres(file_size)
        value = block_count*block_size
        self.progles.set(value)

    def _popup_progres(self, file_size):
        self.popup_flag = True
        self.popup = tk.Toplevel(self)
        self.popup.geometry("200x50")
        build_prg_label = ttk.Label(self.popup, text="進捗")
        build_prg_prg = ttk.Progressbar(self.popup,maximum=file_size,mode="determinate",
                                        variable=self.progles, length=180)
        
        build_prg_label.grid(row=0,column=0)
        build_prg_prg.grid(row=1, column=0, padx=10)

    def _build_sv(self):
        try:
            self.build_buildbutton["state"] = tk.DISABLED
            self.popup_flag = False
            self.builds = BuildSV()
            self.builds.sv_build(
                self.pjname.get(),
                self.build_url[self.svver.get()],
                self.svver.get(),
                self.svmemmin.get(),
                self.svmemmax.get(),
                world_path=self.worldpath.get(),
                server_property=self.svcnf.get(),
                server_ops=self.ops.get(),
                server_whitelist=self.whitelist.get(),
                set_bef=self.st_stsetstext_bef.get('1.0', 'end'),
                set_aft=self.st_stsetstext_aft.get('1.0', 'end'),
                collback=self._printsarg
                )
            self.build_buildbutton["state"] = tk.NORMAL
            try:
                self.popup.destroy()
            except:
                pass
            if self.builds.rename_er == 0:
                messagebox.showinfo("","作成しました")
            else:
                messagebox.showinfo("",f"同じ名前が存在したため{self.pjname.get()}({self.builds.rename_er})として作成しました")
            del self.builds
        except Exception as e:
            self.build_buildbutton["state"] = tk.NORMAL
            messagebox.showerror("",f"{e}")

    def set_place(self):
        self.pj.place(x=10, y=10)
        self.sv.place(x=10, y=75)
        self.st.place(x=10, y=300)
        self.buildsv.place(x=480, y=280)
        self.pj_name.grid(row=0, column=0)
        self.sv_ver.grid(row=0, column=0, sticky=tk.W)
        self.sv_cnf.grid(row=1, column=0, sticky=tk.W)
        self.sv_mem.grid(row=2, column=0, sticky=tk.W)
        self.sv_jarg.grid(row=3,column=0, sticky=tk.W)
        self.sv_world.grid(row=4, column=0, sticky=tk.W)
        self.sv_ops.grid(row=0, column=1)
        self.sv_white.grid(row=1, column=1)
        self.st_sets.grid(row=0, column=0)
