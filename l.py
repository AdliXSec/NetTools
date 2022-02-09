import os, time, socket, platform, hashlib, requests, json, base64

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

def getIP():
    os.system(hapus)
    host = input(" url: ")
    print(cyan+" IP nya: ",red, socket.gethostbyname(host))

def tracerouter():
    os.system(hapus)
    ip = input("IP address target : ")
    results = os.popen("pathping "+str(ip))
    for i in results:
        print(i)

def hashmd5():
    os.system(hapus)
    text = input(" nilai string : ")
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    print(" nilai hash md5 : ",greenLight, md5.hexdigest())

def hashsha():
    os.system(hapus)
    text = input(" nilai string : ")
    sha = hashlib.sha1()
    sha.update(text.encode("utf-8"))
    print(" nilai hash sha1 : ",greenLight, sha.hexdigest())

def md5crack():
    os.system(hapus)
    md5_c = input("Masukan md5 : ")
    pwd = open("password.txt", 'r')
    for password in pwd:
        md5 = hashlib.md5()
        md5.update(password.strip().encode('utf-8'))
        print("Coba Password : ", password.strip())
        if md5_c.strip() == md5.hexdigest():
            print("\n"+greenLight+"Password ditemukan : ", password.strip())
            break
    else:
        print(red+"Password Tidak ditemukan")

def sha1crack():
    os.system(hapus)
    sha1_c = input("Masukan sha1 : ")
    pwd = open("password.txt", 'r')
    for password in pwd:
        sha = hashlib.sha1()
        sha.update(password.strip().encode('utf-8'))
        print("Coba Password : ", password.strip())
        if sha1_c.strip() == sha.hexdigest():
            print("\n"+greenLight+"Password ditemukan : ", password.strip())
            break
    else:
        print(red+"Password Tidak ditemukan")

def tcpsweep():
    os.system(hapus)
    net = input("IP Address : ")
    net1 = net.split(".")
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("Nomor IP Awal : "))
    en1 = int(input("Nomor IP AKhir : "))
    port = int(input("Nomor Port : "))
    en1=en1+1
    def scan(addr):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr,port))
        if result == 0:
            return 1
        else:
            return 0

    def run1():
        for ip in range(st1,en1):
            addr = net2+str(ip)
            if (scan(addr)):
                print(addr, " Hidup")
    run1()

def ipgeo():
    os.system(hapus)
    ipaddr = input(" Ip Address : ")
    ipreq = requests.get(f"http://ip-api.com/json/{ipaddr}")

    if ipreq.status_code == 200:
        ipdata = json.loads(ipreq.text)

        if ipdata["status"] == "success":
            for key in ipdata:
                print(f"{cyan} {key.capitalize()} : {red}{ipdata[key]}")
                
                if key == "lon":
                    lat = ipdata["lat"]
                    lon = ipdata["lon"]
                    maps = f"https://www.google.com/maps/@{lat},{lon},9z"
                    print(f" {cyan}Maps : {yellow}{maps}")

def installing():
    os.system(hapus)
    os.system("pip install requests")

def b64encode():
    os.system(hapus)
    sample_string = input(" Masukkan String : ")
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    print(f"{cyan} Encoded string: {red}{base64_string}")

def b64decode():
    os.system(hapus)
    sample_string = input(" Masukkan base64 : ")
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64decode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    print(f"{cyan} Decoded string: {red}{base64_string}")

def passwordGenerator():
    os.system(hapus)
    text = input(" nilai string : ")
    sha1 = hashlib.sha1()
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha384()
    sha512 = hashlib.sha512()

    sha1.update(text.encode("utf-8"))
    md5.update(text.encode("utf-8"))
    sha256.update(text.encode("utf-8"))
    sha384.update(text.encode("utf-8"))
    sha512.update(text.encode("utf-8"))
    print(cyan+" Password hash sha1 : ",red, sha1.hexdigest())
    print(cyan+" Password hash md5 : ",red, md5.hexdigest())
    print(cyan+" Password hash sha256 : ",red, sha256.hexdigest())
    print(cyan+" Password hash sha384 : ",red, sha384.hexdigest())
    print(cyan+" Password hash sha512 : ",red, sha512.hexdigest())