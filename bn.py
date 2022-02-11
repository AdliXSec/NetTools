import os
import platform

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

def biphost():
    print(cyan+''' 
      _____      _     _____ _____  
     / ____|    | |   |_   _|  __ \ 
    | |  __  ___| |_    | | | |__) |
    | | |_ |/ _ \ __|   | | |  ___/ 
    | |__| |  __/ |_   _| |_| |     
     \_____|\___|\__| |_____|_|     
    ---------------------------------
     \n''')

def btrcip():
    print(cyan+''' 
      _______ _____            _____ ______ _____   ____  _    _ _______ ______   _____ _____  
     |__   __|  __ \     /\   / ____|  ____|  __ \ / __ \| |  | |__   __|  ____| |_   _|  __ \ 
        | |  | |__) |   /  \ | |    | |__  | |__) | |  | | |  | |  | |  | |__      | | | |__) |
        | |  |  _  /   / /\ \| |    |  __| |  _  /| |  | | |  | |  | |  |  __|     | | |  ___/ 
        | |  | | \ \  / ____ \ |____| |____| | \ \| |__| | |__| |  | |  | |____   _| |_| |     
        |_|  |_|  \_\/_/    \_\_____|______|_|  \_|\____/ \____/   |_|  |______| |_____|_|     
    -------------------------------------------------------------------------------------------
     \n''')

def bhmd5():
    print(cyan+''' 
      _    _           _       __  __     _ _____ 
     | |  | |         | |     |  \/  |   | | ____|
     | |__| | __ _ ___| |__   | \  / | __| | |__  
     |  __  |/ _` / __| '_ \  | |\/| |/ _` |___ \ 
     | |  | | (_| \__ \ | | | | |  | | (_| |___) |
     |_|  |_|\__,_|___/_| |_| |_|  |_|\__,_|____/ 
    -----------------------------------------------
     \n''')

def bhsha1():
    print(cyan+''' 
     _    _           _        _____ _          __ 
    | |  | |         | |      / ____| |        /_ |
    | |__| | __ _ ___| |__   | (___ | |__   __ _| |
    |  __  |/ _` / __| '_ \   \___ \| '_ \ / _` | |
    | |  | | (_| \__ \ | | |  ____) | | | | (_| | |
    |_|  |_|\__,_|___/_| |_| |_____/|_| |_|\__,_|_|
    -----------------------------------------------
     \n''')

def bmd5c():
    print(cyan+''' 
     __  __     _ _____    _____                _    
    |  \/  |   | | ____|  / ____|              | |   
    | \  / | __| | |__   | |     _ __ __ _  ___| | __
    | |\/| |/ _` |___ \  | |    | '__/ _` |/ __| |/ /
    | |  | | (_| |___) | | |____| | | (_| | (__|   < 
    |_|  |_|\__,_|____/   \_____|_|  \__,_|\___|_|\_|
    -----------------------------------------------
     \n''')

def bsha1c():
    print(cyan+''' 
      _____ _          __    _____                _    
     / ____| |        /_ |  / ____|              | |   
    | (___ | |__   __ _| | | |     _ __ __ _  ___| | __
     \___ \| '_ \ / _` | | | |    | '__/ _` |/ __| |/ /
     ____) | | | | (_| | | | |____| | | (_| | (__|   < 
    |_____/|_| |_|\__,_|_|  \_____|_|  \__,_|\___|_|\_|
    -----------------------------------------------
     \n''')

def btcpsweep():
    print(cyan+''' 
      _______ _____ _____     _____                        
     |__   __/ ____|  __ \   / ____|                       
        | | | |    | |__) | | (_____      _____  ___ _ __  
        | | | |    |  ___/   \___ \ \ /\ / / _ \/ _ \ '_ \ 
        | | | |____| |       ____) \ V  V /  __/  __/ |_) |
        |_|  \_____|_|      |_____/ \_/\_/ \___|\___| .__/ 
    ------------------------------------------------| |----    
                                                    |_|    
     \n''')

def bipgeo():
    print(cyan+''' 
     _____ _____     _____            
    |_   _|  __ \   / ____|           
      | | | |__) | | |  __  ___  ___  
      | | |  ___/  | | |_ |/ _ \/ _ \ 
     _| |_| |      | |__| |  __/ (_) |
    |_____|_|       \_____|\___|\___/
    ----------------------------------
     \n''')

def bb64enc():
    print(cyan+''' 
     ____    __ _  _     ______            
    |  _ \  / /| || |   |  ____|           
    | |_) |/ /_| || |_  | |__   _ __   ___ 
    |  _ <| '_ \__   _| |  __| | '_ \ / __|
    | |_) | (_) | | |   | |____| | | | (__ 
    |____/ \___/  |_|   |______|_| |_|\___|
    ----------------------------------
     \n''')

def bb64dcd():
    print(cyan+''' 
     ____    __ _  _     _____            
    |  _ \  / /| || |   |  __ \           
    | |_) |/ /_| || |_  | |  | | ___  ___ 
    |  _ <| '_ \__   _| | |  | |/ _ \/ __|
    | |_) | (_) | | |   | |__| |  __/ (__ 
    |____/ \___/  |_|   |_____/ \___|\___|
    ----------------------------------
     \n''')

def bpwg():
    print(cyan+''' 
     _____              _____                           _             
    |  __ \            / ____|                         | |            
    | |__) |_      __ | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
    |  ___/\ \ /\ / / | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    | |     \ V  V /  | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
    |_|      \_/\_/    \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
    ----------------------------------
     \n''')