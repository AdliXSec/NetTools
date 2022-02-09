from hashlib import md5
from l import *

brown = "\033[33m"
greenLight = "\033[32m"
cyan = "\033[36m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
white = "\033[37m"
purple = "\033[35m"

def menu():
    print("\n")
    print(blue+" ============== MENU ==============")
    print(" |                                |")
    print(cyan+"   [1] Get IP From Host Name       ")
    print("   [2] TRACEROUTE IP               ")
    print("   [3] Hash Md5                    ")
    print("   [4] Hash sha1                   ")
    print("   [5] Md5 Cracking                ")
    print("   [6] Sha1 Cracking               ")
    print("   [7] TCP Sweep                   ")
    print("   [8] IP GeoLocation              ")
    print("   [9] Base64 Encode               ")
    print("   [10] Base64 Decode              ")
    print("   [11] Password Generator         ")
    print("   [x] Installing                  ")
    print("   [0] LogOut :)                   ")
    print(blue+" |                                |")
    print(" ==================================")
    print(blue+" ==================================")
    print(" |")
    pilih = input(" |= Select Menu => ")
    print("\n")

    if pilih == str(1):
        getIP()
    elif pilih == str(2):
        tracerouter()
    elif pilih == str(3):
        hashmd5()
    elif pilih == str(4):
        hashsha()
    elif pilih == str(5):
        md5crack()
    elif pilih == str(6):
        sha1crack()
    elif pilih == str(7):
        tcpsweep()
    elif pilih == str(8):
        ipgeo()
    elif pilih == str(9):
        b64encode()
    elif pilih == str(10):
        b64decode()
    elif pilih == str(11):
        passwordGenerator()
    elif pilih == "x":
        installing()
    elif pilih == str(0):
        print(greenLight+" Terimakasih Telah Berkunjung")
        exit()
    
    


