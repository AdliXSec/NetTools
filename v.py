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
yellow = "33[33;1m"


def view1():
    os.system(hapus)
    print("")
    print("  "+blue+" _   _      _     _______          _           ")
    print("  "+blue+"| \ | |    | |   |__   __|        | |          ")
    print("  "+blue+"|  \| | ___| |_     | | ___   ___ | |___       ")
    print("  "+blue+"| . ` |/ _ \ __|    | |/ _ \ / _ \| / __|      ")
    print("  "+blue+"| |\  |  __/ |_     | | (_) | (_) | \__ \      ")
    print("  "+blue+"|_| \_|\___|\__|    |_|\___/ \___/|_|___/      ")
    print("  "+yellow+"-----------------------------------------      ")
    print("")
    print(" "+blueLight+"[+] Author                : AdliXSec            ")
    print(" "+blueLight+"[+] Team                  : Dark Clown Security ")
    print(" "+blueLight+"[+] Versi                 : 0.1.0               ")
    print("")

def infouser():
    print("             "+yellow+"Informasion System                  ")
    print("")
    print(" "+blueLight+"[+] OS                    : ",platform.system())
    print(" "+blueLight+"[+] Processor             : ",platform.processor())
    print(" "+blueLight+"[+] Machine               : ",platform.machine())
    print(" "+blueLight+"[+] System's network name : ",platform.node())
    print(" "+blueLight+"[+] Platform Information  : ",platform.platform())
                              