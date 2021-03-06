from genericpath import exists
from os import mkdir

def setup():
    make_dir()
    add_file()

def make_dir():
    if not exists("./server"): mkdir("./server")
    if not exists("./data/"): mkdir("./data/")
    if not exists("./data/config"): mkdir("./data/config")
    if not exists("./data/whitelist"): mkdir("./data/whitelist")
    if not exists("./data/sv_properties"): mkdir("./data/sv_properties")
    if not exists("./data/ops"): mkdir("./data/ops")
    if not exists("./data/banned_ips"): mkdir("./data/banned_ips")
    if not exists("./data/banned_players"): mkdir("./data/banned_players")
    if not exists("./data/sv_cache"): mkdir("./data/sv_cache")

def add_file():
    if not exists("./data/config/svcnfdata.json"):
        with open("./data/config/svcnfdata.json","w") as f:
            f.write("""{
    "str_obj": {
        "server-ip": [
            {"text": "server-ip"},
            {"width": 30, "textvariable": ["serverip", ""]}
        ],
        "resource-pack": [
            {"text": "resource-pack"},
            {"width": 30, "textvariable": ["resourcepack", ""]}
        ],
        "resource-pack-sha1": [
            {"text": "resource-pack-sha1"},
            {"width": 30, "textvariable": ["resourcepacksha1", ""]}
        ],
        "rcon.password": [
            {"text": "rcon.password"},
            {"width": 30, "textvariable": ["rconpassword", ""]}
        ],
        "rmotd": [
            {"text": "motd"},
            {"width": 30, "textvariable": ["rmotd", ""]}
        ],
        "level-type": [
            {"text": "level-type"},
            {"width": 30, "textvariable": ["leveltype", ""]}
        ],
        "level-seed": [
            {"text": "level-seed"},
            {"width": 30, "textvariable": ["levelseed", ""]}
        ],
        "level-name": [
            {"text": "level-name"},
            {"width": 30, "textvariable": ["levelname", "world"]}
        ],
        "generator-settings": [
            {"text": "level-seed"},
            {"width": 30, "textvariable": ["generatorsettings", ""]}
        ],
        "difficulty": [
            {"text": "difficulty"},
            {"width": 30, "textvariable": ["difficulty", "easy"]}
        ],
        "gamemode": [
            {"text": "gamemode"},
            {"width": 30, "textvariable": ["gamemode", "survival"]}
        ],
        "motd": [
            {"text": "motd"},
            {"width": 30, "textvariable": ["motd", "A Minecraft Server"]}
        ],
        "text-filtering-config": [
            {"text": "text-filtering-config"},
            {"width": 30, "textvariable": ["textfilteringconfig", ""]}
        ],
        "resource-pack-prompt": [
            {"text": "resource-pack-prompt"},
            {"width": 30, "textvariable": ["resourcepackprompt", ""]}
        ],
        "require-resource-pack": [
            {"text": "require-resource-pack"},
            {"width": 30, "textvariable": ["requireresourcepack", ""]}
        ]
    },
    "int_obj": {
        "view-distance": [
            {"text": "view-distance"},
            {"width": 10, "from_": 2, "to": 32, "increment": 1, "textvariable": ["viewdistance", 10]}
        ],
        "spawn-protection": [
            {"text": "spawn-protection"},
            {"width": 10, "from_": 0, "to": 2147483647, "increment": 1, "textvariable": ["spawnprotection", 16]}
        ],
        "server-port": [
            {"text": "server-port"},
            {"width": 10, "from_": 1, "to": 65534, "increment": 1, "textvariable": ["serverport", 25565]}
        ],
        "rcon.port": [
            {"text": "rcon.port"},
            {"width": 10, "from_": 0, "to": 0, "increment": 0, "textvariable": ["rconport", 25575]}
        ],
        "rate-limit": [
            {"text": "rate-limit"},
            {"width": 10, "from_": 0, "to": 1500, "increment": 100, "textvariable": ["ratelimit", 0]}
        ],
        "query.port": [
            {"text": "query.port"},
            {"width": 10, "from_": 1, "to": 65534, "increment": 1, "textvariable": ["queryport", 25565]}
        ],
        "player-idle-timeout": [
            {"text": "player-idle-timeout"},
            {"width": 10, "from_": 0, "to": 2147483647, "increment": 10, "textvariable": ["playeridletimeout", 0]}
        ],
        "op-permission-level": [
            {"text": "op-permission-level"},
            {"width": 10, "from_": 1, "to": 4, "increment": 1, "textvariable": ["oppermissionlevel", 4]}
        ],
        "network-compression-threshold": [
            {"text": "network-compression-threshold"},
            {"width": 10, "from_": -1, "to": 1500, "increment": 1, "textvariable": ["networkcompressionthreshold", 256]}
        ],
        "max-world-size": [
            {"text": "max-world-size"},
            {"width": 10, "from_": 1, "to": 29999984, "increment": 0, "textvariable": ["maxworldsize", 29999984]}
        ],
        "max-tick-time": [
            {"text": "max-tick-time"},
            {"width": 10, "from_": -1, "to": 9223372036854775807, "increment": 1000, "textvariable": ["maxticktime", 60000]}
        ],
        "max-players": [
            {"text": "max-players"},
            {"width": 10, "from_": 0, "to": 100, "increment": 1, "textvariable": ["maxplayers", 20]}
        ],
        "max-build-height": [
            {"text": "max-build-height"},
            {"width": 10, "from_": 1, "to": 512, "increment": 1, "textvariable": ["maxbuildheight", 256]}
        ],
        "function-permission-level": [
            {"text": "function-permission-level"},
            {"width": 10, "from_": 1, "to": 4, "increment": 1, "textvariable": ["functionpermissionlevel", 2]}
        ],
        "entity-broadcast-range-percentage": [
            {"text": "entity-broadcast-range-percentage"},
            {"width": 10, "from_": 0, "to": 500, "increment": 1, "textvariable": ["entitybroadcastrangepercentage", 100]}]
    },
    "bool_obj": {
        "enforce-whitelist": [
            {"text": "enforce-whitelist"},
            {"variable": ["enforcewhitelist", false]}
        ],
        "whitelist": [
            {"text": "whitelist"},
            {"variable": ["whitelist", false]}
        ],
        "use-native-transport": [
            {"text": "use-native-transport"},
            {"variable": ["usenativetransport", true]}
        ],
        "spawn-npcs": [
            {"text": "spawn-npcs"},
            {"variable": ["spawnnpcs", true]}
        ],
        "spawn-monstar": [
            {"text": "spawn-monsters"},
            {"variable": ["spawnmonsters", true]}
        ],
        "spawn-animals": [
            {"text": "spawn-animals"},
            {"variable": ["spawnanimals", true]}
        ],
        "snooper-enabled": [
            {"text": "snooper-enabled"},
            {"variable": ["snooperenabled", true]}
        ],
        "prevent-proxy-connections": [
            {"text": "prevent-proxy-connections"},
            {"variable": ["preventproxyconnections", false]}
        ],
        "online-mode": [
            {"text": "online-mode"},
            {"variable": ["onlinemode", true]}
        ],
        "hardcore": [
            {"text": "hardcore"},
            {"variable": ["hardcore", false]}
        ],
        "generate-structures": [
            {"text": "generate-structures"},
            {"variable": ["generatestructures", true]}
        ],
        "force-gamemode": [
            {"text": "force-gamemode"},
            {"variable": ["forcegamemode", false]}
        ],
        "enable-query": [
            {"text": "enable-query"},
            {"variable": ["enablequery", false]}
        ],
        "enable-jmx-monitoring": [
            {"text": "enable-jmx-monitoring"},
            {"variable": ["enablejmxmonitoring", false]}
        ],
        "broadcast-rcon-to-ops": [
            {"text": "broadcast-rcon-to-ops"},
            {"variable": ["broadcastrcontoops", true]}
        ],
        "broadcast-console-to-ops": [
            {"text": "broadcast-console-to-ops"},
            {"variable": ["broadcastconsoletoops", true]}
        ],
        "allow-nether": [
            {"text": "allow-nether"},
            {"variable": ["allownether", true]}
        ],
        "allow-flight": [
            {"text": "allow-flight"},
            {"variable": ["allowflight", false]}
        ],
        "sync-chunk-writes": [
            {"text": "sync-chunk-writes"},
            {"variable": ["syncchunkwrites", true]}
        ],
        "enable-status": [
            {"text": "enable-status"},
            {"variable": ["enablestatus", true]}
        ],
        "enable-command-block": [
            {"text": "enable-command-block"},
            {"variable": ["enablecommandblock", false]}
        ],
        "pvp": [
            {"text": "pvp"},
            {"variable": ["pvp", true]}
        ],
        "enable-rcon": [
            {"text": "enable-rcon"},
            {"variable": ["enablercon", false]}]
    }
}""")
