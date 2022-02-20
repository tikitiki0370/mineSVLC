from os import mkdir
from os.path import exists


def build_svpr(name, payload):
    var_name_ls = ['spawn-protection', 'max-tick-time', 'query.port', 'generator-settings', 
                'sync-chunk-writes', 'force-gamemode', 'allow-nether', 'enforce-whitelist', 
                'gamemode', 'broadcast-console-to-ops', 'enable-query', 'player-idle-timeout', 
                'text-filtering-config', 'difficulty', 'broadcast-rcon-to-ops', 'spawn-monsters', 
                'op-permission-level', 'pvp', 'entity-broadcast-range-percentage', 'snooper-enabled', 
                'level-type', 'enable-status', 'resource-pack-prompt', 'hardcore', 'enable-command-block', 
                'network-compression-threshold', 'max-players', 'max-world-size', 'resource-pack-sha1', 
                'function-permission-level', 'rcon.port', 'server-port', 'server-ip', 'spawn-npcs', 
                'require-resource-pack', 'allow-flight', 'level-name', 'view-distance', 'resource-pack', 
                'spawn-animals', 'white-list', 'rcon.password', 'generate-structures', 'online-mode', 
                'level-seed', 'prevent-proxy-connections', 'use-native-transport', 'enable-jmx-monitoring', 
                'motd', 'rate-limit', 'enable-rcon']

    write_str = "#Minecraft server properties\n#generate by mineSVLC\n"
    for i in var_name_ls:
        temp = i.replace("-", "").replace(".", "")
        value = str(payload[temp])
        write_str += f"{i}={value.lower()}\n"

    if not exists("./data/sv_properties"):
        mkdir("./data/sv_properties/")
    with open(f"./data/sv_properties/{name}.properties", "w") as f:
        f.write(write_str)

def load_file(name, func):
    return_dict = {}
    with open(f"./data/sv_properties/{name}.properties") as f:
        read_str = f.read()
        for i in read_str.split("\n"):
            if not i:
                continue
            if i[0] == "#":
                continue
            key = i[0:i.index("=")].replace("-", "").replace(".", "")
            value = i[i.index("=")+1:]
            if value == "false" or value == "true":
                return_dict[key] = False if value == "false" else True
            elif value.isdecimal() == True:
                return_dict[key] = int(value)
            else:
                return_dict[key] = value
        func(return_dict)
