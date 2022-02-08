from hashlib import md5
from library import *

def menu():
    print("\n")
    print(" ============== MENU ==============")
    print(" |                                |")
    print(" | [1] Get IP From Host Name      |")
    print(" | [2] TRACEROUTE IP              |")
    print(" | [3] Hash Md5                   |")
    print(" | [4] Hash sha1                  |")
    print(" | [5] Md5 Cracking               |")
    print(" | [6] Sha1 Cracking              |")
    print(" | [7] TCP Sweep                  |")
    print(" | [8] IP GeoLocation             |")
    print(" | [9] Installing                 |")
    print(" | [0] LogOut :)                  |")
    print(" |                                |")
    print(" ==================================")
    print(" ==================================")
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
    
    


