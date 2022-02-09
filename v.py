import os
import platform

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

def view1():
    os.system(hapus)
    print(" ======================================================================")
    print(" #                                                                    #")
    print(" #              _   _      _     _______          _                   #")
    print(" #             | \ | |    | |   |__   __|        | |                  #")
    print(" #             |  \| | ___| |_     | | ___   ___ | |___               #")
    print(" #             | . ` |/ _ \ __|    | |/ _ \ / _ \| / __|              #")
    print(" #             | |\  |  __/ |_     | | (_) | (_) | \__ \              #")
    print(" #             |_| \_|\___|\__|    |_|\___/ \___/|_|___/              #")
    print(" #    ------------------------------------------------------------    #")
    print(" #    [+] Author : AdliXSec                     [+] Versi  : 0.1.0    #")
    print(" #    [+] Team   : Dark Clown Security                                #")
    print(" #                                                                    #")
    print(" #                                                                    #")  
    print(" ======================================================================")      

def infouser():
    print("\n")
    print(" ========================= Information User ============================")
    print(" #                                                                     #")  
    print(" #   OS                    : ",platform.system())
    print(" #   Processor             : ",platform.processor())
    print(" #   Machine               : ",platform.machine())
    print(" #   System's network name : ",platform.node())
    print(" #   Platform Information  : ",platform.platform())
    print(" #                                                                     #")
    print(" =======================================================================")
                              