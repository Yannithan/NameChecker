import requests
import string
import pathlib
import colorama
import os, sys
import time
from pathlib import Path
from colorama import *

os.system("title [Minecraft] Username Checker by - Yanny")
current_path = os.path.dirname(os.path.realpath(__file__))
open(current_path +"/"+str("Available")+str("")+".txt","a") #Create the Available.txt
open(current_path +"/"+str("Usernames")+str("")+".txt","a") #Create the Usernames.txt
names = open('Usernames.txt', 'r')
available = open('Available.txt', 'w')
mypath = Path('Usernames.txt')

def check():
    os.system("cls")
    print(Fore.LIGHTBLACK_EX+"["+Fore.CYAN+"+"+Fore.LIGHTBLACK_EX+"]"+" Minecraft Username Checker by Yanny")

    if mypath.stat().st_size == 0:
        print(Fore.WHITE+"\nPlease put your names in Usernames.txt"+ Fore.RED +"\nClosing in 5 seconds")
        time.sleep(5)
        sys.exit()
    else:
           pass   
    with open('Usernames.txt', 'r') as f:
            for line in f:
                time.sleep(0)
                nick = line.rstrip("\n")
                src = requests.get('https://account.mojang.com/available/minecraft/'+nick)
                if src.text == "TAKEN":
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"Taken"+Fore.WHITE+"] "+Fore.RESET + nick)
                else:
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"Not Taken"+Fore.WHITE+"] "+Fore.RESET+ nick)

check()

print(Fore.CYAN+"\nChecker finished.")
print("Available usernames saved!")
print(Fore.RED +"Closing in 5 seconds")
time.sleep(5)
sys.exit()
