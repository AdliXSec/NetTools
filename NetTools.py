from v import *
from m import *
import os
import platform

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