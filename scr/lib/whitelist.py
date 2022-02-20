from json import JSONDecodeError, dump, load, loads
from os import mkdir
from os.path import exists
from urllib.request import urlopen


class BuildWls():
    def __init__(self):
        self.write_data = []
        self.file = None
        self.loop_count = 0

    def __del__(self):
        self.__file_close()

    def __file_close(self):
        try:
            self.file.close()
        except:
            pass

    def load_whitelist(self, file_name):
        self.__file_close()
        self.file = open(f"./data/whitelist/{file_name}.json", mode="r")
        try:
            self.write_data = load(self.file)
        except JSONDecodeError:
            pass
        self.__file_close()
        self.file = open(f"./data/whitelist/{file_name}.json", mode="w")

    def _open_editfile(self, file_name, loop_count=0):
        self.__file_close()
        if not exists("./data/whitelist"):
            mkdir("./data/whitelist")
            self.file = open(f"./data/whitelist/{file_name}.json", mode="w")
            return loop_count
        elif not exists(f"./data/whitelist/{file_name}.json"):
            self.file = open(f"./data/whitelist/{file_name}.json", mode="w")
            return loop_count
        else:
            if loop_count != 0:
                file_name = file_name[:-(len(str(loop_count+1))+2)]
            return self._open_editfile(f"{file_name}({loop_count+1})", loop_count=loop_count+1)

    def __serch_player_uuid(self, name):
        api_path = f"https://api.mojang.com/users/profiles/minecraft/{name}"
        data = loads(urlopen(api_path).read().decode("utf8"))
        return data

    def deta_del(self, name):
        data = self.__serch_player_uuid(name)
        data_ls = {"uuid":data["id"].replace("-", ""), "name":data["name"]}
        if data_ls in self.write_data: 
            self.write_data.remove(data_ls)

    def deta_add(self, name):
        data = self.__serch_player_uuid(name)
        data_ls = {"uuid":data["id"].replace("-", ""), "name":data["name"]}
        if data_ls in self.write_data: 
            self.write_data.remove(data_ls)
            self.write_data.append(data_ls)
        else:
            self.write_data.append(data_ls)

    def deta_collback(self, fung):
        return fung(self.write_data)

    def create_wls(self, file_name=None):
        self.loop_count = 0
        if not self.file:
            self.loop_count = self._open_editfile(file_name)
        dump(self.write_data, self.file, indent=4)
        self.file.close()
        self.file = None
        self.write_data = []
