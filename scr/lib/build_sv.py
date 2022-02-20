from hashlib import sha1
from json import loads
from os import makedirs, rename
from shutil import copy, copytree, rmtree
from urllib.request import urlopen, urlretrieve


class BuildSV():
    def __init__(self):
        try:
            makedirs("./server/temp")
        except FileExistsError:
            rmtree("./server/temp")
            makedirs("./server/temp")
        self.rename_er = 0
        self.download_count = 0
        self.download_blocksize = 0
        self.download_size = 0

    def __del__(self):
        try:
            rmtree("./server/temp")
        except FileNotFoundError:
            pass

    def get_prg(self):
        print(self.download_count * self.download_blocksize)


    def _file_download(self, download_path):
        #サーバーダウンロードpath取得
        data = loads(urlopen(download_path).read().decode("utf8"))
        download_path = data["downloads"]["server"]["url"]
        download_hash = data["downloads"]["server"]["sha1"]
        #サーバーダウンロード
        urlretrieve(download_path, "server/temp/server.jar", self.collbackpoint)
        #ハッシュチェック
        with open(f"server/temp/server.jar", "rb") as f:
            file_data = f.read()
            if not sha1(file_data).hexdigest() == download_hash:
                raise ValueError

    def _mkbatfile(self, memor_min, memor_max, set_bfe, set_aft):
        #内容生成
        write_ls = [f"{set_bfe}", 
                    f"java -server -Xmx{memor_max}M -Xms{memor_min}M -jar server.jar\n",
                    f"{set_aft}"]
        with open("server/temp/start.bat", "w") as f:
            f.writelines(write_ls)

    def _rename_dir(self, dir_name):
        try:
            rename("./server/temp",f"./server/{dir_name}")
        except FileExistsError:
            self.rename_er += 1
            self._rename_dir(f"{dir_name}({self.rename_er})")

    def _set_property(self, name):
        if not name:
            return
        copy(f"./data/sv_properties/{name}.properties", "./server/temp/server.properties")

    def _set_ops(self, name):
        if not name:
            return
        copy(f"./data/ops/{name}.json", "./server/temp/ops.json")

    def _set_whitelist(self, name):
        if not name:
            return
        copy(f"./data/ops/{name}.json", "./server/temp/whitelist.json")

    def _set_worldfile(self, world_path):
        if world_path:
            copytree(world_path,"./server/temp/world")


    def sv_build(self, folder_name, file_url, server_version, memor_min, memor_max, 
                    arg_jvm=None, server_property=None, world_path=None, server_ops=None, server_whitelist=None, set_bef=None, set_aft=None, collback=None):
        self.collbackpoint = collback
        self._file_download(file_url)
        self._mkbatfile(memor_min, memor_max, set_bef, set_aft)
        self._set_worldfile(world_path)
        self._set_property(server_property)
        self._set_ops(server_ops)
        self._set_whitelist(server_whitelist)
        self._rename_dir(folder_name)

