import os
import platform

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

def view1():
    os.system(hapus)
    print(" ================================================")
    print(" #                                              #")
    print(" #    _   _      _     _______          _       #")
    print(" #   | \ | |    | |   |__   __|        | |      #")
    print(" #   |  \| | ___| |_     | | ___   ___ | |___   #")
    print(" #   | . ` |/ _ \ __|    | |/ _ \ / _ \| / __|  #")
    print(" #   | |\  |  __/ |_     | | (_) | (_) | \__ \  #")
    print(" #   |_| \_|\___|\__|    |_|\___/ \___/|_|___/  #")
    print(" #   -----------------------------------------  #")
    print(" #   Author : AdliXSec                          #")
    print(" #   Team   : Dark Clown Security               #")
    print(" #   Versi  : 0.1.0                             #")
    print(" #                                              #")  
    print(" ================================================")                                    