from v import *
from m import *
import os
import platform
import hashlib
import msvcrt

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

def getPass():
    passw = ''
    print(" # Masukkan Password ",greenLight, end='', flush=True)
    while True:
        x = msvcrt.getch().decode("utf-8")
        if x == '\r' or x == '\n':
            break
        print('*', end='', flush=True)
        passw +=x
    return passw
    
os.system(hapus)
jawab = "y"
password = "0e40043cd9419473cecd3f56b625d337"
view1()
print(cyan+" ==========================================")
print(" #")
intPassword = getPass()
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