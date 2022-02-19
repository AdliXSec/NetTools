from v import ins
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

while(True):
    ins()
    print(blue+" ==================================")
    print(" |")
    pilih = input(" |= Select Menu => "+cyan)
    print("\n")
    if pilih == str(1):
        break
    elif pilih == str(2):
        os.system(hapus)
        os.system("python3 -m pip install --upgrade pip")
        os.system("pip install requests")
        print(greenLight+" Password : NetTools \n")
        tanya = input( "Login? (y/n) : ")
        if tanya == "y":
            break
        elif tanya == "n":
            exit()
    elif pilih == str(3):
        exit()

from v import *
from m import *
import os
import platform
import hashlib
import getpass

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
    
os.system(hapus)
jawab = "y"
password = "0e40043cd9419473cecd3f56b625d337"
view1()
print(cyan+" ==========================================")
print(" #")

intPassword = getpass.getpass(" #== Masukkan Password ==> ")

sha = hashlib.md5()
sha.update(intPassword.encode("utf-8"))
if(sha.hexdigest() == password):
    while(jawab == "y"):
        view1()
        infouser()
        menu()
        print("")
        jawab = input(cyan+" Lanjut Lagi? (y/n) : ")
        if(jawab == 'n'):
            print("")
            print(greenLight+" Terimakasih Telah Berkunjung \n")
            exit()
else:
    view1()
    print(white+" Password "+red+intPassword+" SALAH \n")