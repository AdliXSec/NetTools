from v import *
from m import *
import os
import platform

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

def warna(platform):
    if platform == "Windows":
        os.system("color a")
    else:
        print("\033[92m")

os.system(hapus)
warna(platform.system())
jawab = "y"
while(jawab == "y"):
    view1()
    infouser()
    menu()
    print("")
    jawab = input(" Lanjut Lagi? (y/n) : ")
    if(jawab == 'n'):
        print("")
        print(" Terimakasih Telah Berkunjung")
        exit()