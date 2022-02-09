from v import *
from m import *
import os
import platform

brown = "\033[33m"
greenLight = "\033[32m"
cyan = "\033[36m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
white = "\033[37m"
purple = "\033[35m"

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

os.system(hapus)
jawab = "y"
while(jawab == "y"):
    view1()
    infouser()
    menu()
    print("")
    jawab = input(cyan+" Lanjut Lagi? (y/n) : ")
    if(jawab == 'n'):
        print("")
        print(greenLight+" Terimakasih Telah Berkunjung")
        exit()