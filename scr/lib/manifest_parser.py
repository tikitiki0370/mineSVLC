from json import load
from os import getenv

path = f"{getenv('APPDATA')}\.minecraft\\versions\\version_manifest_v2.json"

def parser():
    #マニフェストファイル読み込み
    try:
        load_file = open(path,"r")
        load_json = load(load_file)
        load_file.close()
    except FileNotFoundError:
        raise FileNotFoundError

    #辞書取り出し
    lat_output = load_json["latest"]
    ver_output = load_json["versions"]
    del load_json

    #パース
    ver_ls = [i["id"] for i in ver_output]
    rel_ls = [i["id"] for i in ver_output if i["type"] == "release"]

    url = {i:j["url"] for i,j in zip(ver_ls,ver_output)}

    del ver_output, lat_output

    return ver_ls, rel_ls, url

if __name__ == "__main__":
    print(parser())
