#!usr/bin/python3

# Please help making this app better! I would love to get feedback!
# Made by Matthew C Lopez
# Email: matthew_christ@protonmail.com
# MIT License
# version 0.1
import os
import re
import time
from colorama import Fore

while True: #Makes program loop.
    time.sleep(2)
    # nmap is needed with this first version.
    scan = os.system('sudo nmap -sn 192.168.0.0/24 > nmap.txt')
    # Nmap scannes the network for divices and puts them into a text file.

    #registered mac adresses.
    Matt = ['24:46:C8:4D:36:E4']
    Lexi = ['A4:77:33:87:07:94']

    print()
    print(Fore.CYAN)
    # Lets you know is app is working.
    print("APP is working!")
    print()

    # This will then pull data from the text file.
    with open ("nmap.txt", "r") as file:
        find = file.read().replace('\n', '')
    print()
    
    for i in Matt:
            # If user Matt's mac address is found in text file, program will print 'Matt is here'.
            if re.search(r'\b{}\b'.format(i),find):
                print(Fore.GREEN)
                print('Matt is here')
            else:
                print(Fore.RED)
                print("Can't find user")
                print(Fore.GREEN)
                # If matt is not here, it will print "Can't find user".
    print()
    
    for i in Lexi:

            if re.search(r'\b{}\b'.format(i),find):
                print('Lexi is here')
            else:
                print(Fore.RED)
                print("Can't find user")
                print(Fore.GREEN)
