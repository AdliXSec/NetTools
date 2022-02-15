import os, platform

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

brown = "\033[33m"
greenLight = "\033[32m"
cyan = "\033[36m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
white = "\033[37m"
purple = "\033[35m"

def ins():
    os.system(hapus)
    print("")
    print(cyan+"   _   _      _     _______          _           ")
    print("  | \ | |    | |   |__   __|        | |          ")
    print("  |  \| | ___| |_     | | ___   ___ | |___       ")
    print("  | . ` |/ _ \ __|    | |/ _ \ / _ \| / __|      ")
    print("  | |\  |  __/ |_     | | (_) | (_) | \__ \      ")
    print("  |_| \_|\___|\__|    |_|\___/ \___/|_|___/      ")
    print(yellow+"  __________________________________________      ")
    print("")
    print(red+" [+] Author                : AdliXSec            ")
    print(" [+] Team                  : Dark Clown Security ")
    print(" [+] Versi                 : 2.0.0               ")
    print(" [+] Github                : https://github.com/AdliXSec")
    print("\n")
    print(blue+" =============== Menu =============")
    print(blue+" ||                              "+blue+"||")
    print(blue+" || "+greenLight+"[1] Login                    "+blue+"||")
    print(blue+" || "+greenLight+"[2] Install And Get Password "+blue+"||")
    print(blue+" || "+red+"[3] Logout :)                "+blue+"||")
    print(blue+" ||                              "+blue+"||")
    print(blue+" ==================================")