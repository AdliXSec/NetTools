import os, time, socket, platform, hashlib, requests, json, base64

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

def getIP():
    os.system(hapus)
    host = input(" url: ")
    print(" IP nya: ", socket.gethostbyname(host))

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
    print(" nilai hash md5 : ", md5.hexdigest())

def hashsha():
    os.system(hapus)
    text = input(" nilai string : ")
    sha = hashlib.sha1()
    sha.update(text.encode("utf-8"))
    print(" nilai hash sha1 : ", sha.hexdigest())

def md5crack():
    os.system(hapus)
    md5_c = input("Masukan md5 : ")
    pwd = open("password.txt", 'r')
    for password in pwd:
        md5 = hashlib.md5()
        md5.update(password.strip().encode('utf-8'))
        print("Coba Password : ", password.strip())
        if md5_c.strip() == md5.hexdigest():
            print("\nPassword ditemukan : ", password.strip())
            break
    else:
        print("Password Tidak ditemukan")

def sha1crack():
    os.system(hapus)
    sha1_c = input("Masukan sha1 : ")
    pwd = open("password.txt", 'r')
    for password in pwd:
        sha = hashlib.sha1()
        sha.update(password.strip().encode('utf-8'))
        print("Coba Password : ", password.strip())
        if sha1_c.strip() == sha.hexdigest():
            print("\nPassword ditemukan : ", password.strip())
            break
    else:
        print("Password Tidak ditemukan")

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
                print(f" {key.capitalize()} : {ipdata[key]}")
                
                if key == "lon":
                    lat = ipdata["lat"]
                    lon = ipdata["lon"]
                    maps = f"https://www.google.com/maps/@{lat},{lon},9z"
                    print(f" Maps : {maps}")

def installing():
    os.system(hapus)
    os.system("pip install requests")

def b64encode():
    os.system(hapus)
    sample_string = input(" Masukkan String : ")
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    print(f" Encoded string: {base64_string}")

def b64decode():
    os.system(hapus)
    sample_string = input(" Masukkan base64 : ")
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64decode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    print(f" Decoded string: {base64_string}")