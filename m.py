from hashlib import md5
from l import *
import time

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
    time.sleep(0.1)
    print(cyan+"   [1] Get IP From Host Name       ")
    time.sleep(0.1)
    print("   [2] TRACEROUTE IP               ")
    time.sleep(0.1)
    print("   [3] Hash Md5                    ")
    time.sleep(0.1)
    print("   [4] Hash sha1                   ")
    time.sleep(0.1)
    print("   [5] Md5 Cracking                ")
    time.sleep(0.1)
    print("   [6] Sha1 Cracking               ")
    time.sleep(0.1)
    print("   [7] TCP Sweep                   ")
    time.sleep(0.1)
    print("   [8] IP GeoLocation              ")
    time.sleep(0.1)
    print("   [9] Base64 Encode               ")
    time.sleep(0.1)
    print("   [10] Base64 Decode              ")
    time.sleep(0.1)
    print("   [11] Password Generator         ")
    time.sleep(0.1)
    print("   [12] Password Checker           ")
    time.sleep(0.1)
    print("   [13] Admin Finder               ")
    time.sleep(0.1)
    print("   [14] Clickjacking Tester        ")
    time.sleep(0.1)
    print("   [15] CMS Scanner                ")
    time.sleep(0.1)
    print("   [x] Installing                  ")
    time.sleep(0.1)
    print("   [0] LogOut :)                   ")
    time.sleep(0.1)
    print(blue+" |                                |")
    print(" ==================================")
    print(blue+" ==================================")
    print(" |")
    pilih = input(" |= Select Menu => "+greenLight)
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
    elif pilih == str(12):
        passwordChecker()
    elif pilih == str(13):
        admninfind()
    elif pilih == str(14):
        ClickjackingTester()
    elif pilih == str(15):
        cmsscan()
    elif pilih == "x":
        installing()
    elif pilih == str(0):
        print(greenLight+" Terimakasih Telah Berkunjung \n")
        exit()
    

    
    
