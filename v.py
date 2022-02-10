import os
import platform
import requests
import json

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

ipreq = requests.get(f"http://ip-api.com/json/")

if ipreq.status_code == 200:
    ipdata = json.loads(ipreq.text)

    if ipdata["status"] == "success":
        ip = ipdata["query"]


brown = "\033[33m"
greenLight = "\033[32m"
cyan = "\033[36m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
white = "\033[37m"


def view1():
    os.system(hapus)
    print("")
    print(cyan+"   _   _      _     _______          _           ")
    print("  | \ | |    | |   |__   __|        | |          ")
    print("  |  \| | ___| |_     | | ___   ___ | |___       ")
    print("  | . ` |/ _ \ __|    | |/ _ \ / _ \| / __|      ")
    print("  | |\  |  __/ |_     | | (_) | (_) | \__ \      ")
    print("  |_| \_|\___|\__|    |_|\___/ \___/|_|___/      ")
    print(yellow+"  -----------------------------------------      ")
    print("")
    print(red+" [+] Author                : AdliXSec            ")
    print(" [+] Team                  : Dark Clown Security ")
    print(" [+] Versi                 : 1.2.0               ")
    print("\n")

def infouser():
    print(white+"             Informasion System                  ")
    print("")
    print(brown+" [+] Your IP               : ",ip)
    print(" [+] OS                    : ",platform.system())
    print(" [+] Processor             : ",platform.processor())
    print(" [+] Machine               : ",platform.machine())
    print(" [+] System's network name : ",platform.node())
    print(" [+] Platform Information  : ",platform.platform())
                              