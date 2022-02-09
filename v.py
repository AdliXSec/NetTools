import os
import platform

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

green = "33[0;32m"
greenLight = "33[32;1"
blue = "33[0;36m"
blueLight = "33[36;1m"
red = "33[31;1m"


def view1():
    os.system(hapus)
    print("")
    print("   _   _      _     _______          _           ")
    print("  | \ | |    | |   |__   __|        | |          ")
    print("  |  \| | ___| |_     | | ___   ___ | |___       ")
    print("  | . ` |/ _ \ __|    | |/ _ \ / _ \| / __|      ")
    print("  | |\  |  __/ |_     | | (_) | (_) | \__ \      ")
    print("  |_| \_|\___|\__|    |_|\___/ \___/|_|___/      ")
    print("  -----------------------------------------      ")
    print("")
    print(" [+] Author                : AdliXSec            ")
    print(" [+] Team                  : Dark Clown Security ")
    print(" [+] Versi                 : 0.1.0               ")
    print("")

def infouser():
    print("             Informasion System                  ")
    print("")
    print(" [+] OS                    : ",platform.system())
    print(" [+] Processor             : ",platform.processor())
    print(" [+] Machine               : ",platform.machine())
    print(" [+] System's network name : ",platform.node())
    print(" [+] Platform Information  : ",platform.platform())
                              