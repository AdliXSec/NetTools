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
    print("   [9] Installing                  ")
    print("   [0] LogOut :)                   ")
    print(blue+" |                                |")
    print(" ==================================")
    print(blue+" ==================================")
    print(" |")
    pilih = int(input(" |= Select Menu => "))
    print("\n")

    if pilih == int(1):
        getIP()
    elif pilih == int(2):
        tracerouter()
    elif pilih == int(3):
        hashmd5()
    elif pilih == int(4):
        hashsha()
    elif pilih == int(5):
        md5crack()
    elif pilih == int(6):
        sha1crack()
    elif pilih == int(7):
        tcpsweep()
    elif pilih == int(8):
        ipgeo()
    elif pilih == int(9):
        installing()
    elif pilih == int(0):
        exit()
    
    


