# Use With Python 3
import colorama
from fontstyle import apply
from colorama.ansi import Style
from phonenumbers.phonenumberutil import region_code_for_country_code
from pyfiglet import figlet_format
import requests, re, sys, random, time, os
from colorama import Fore, Back, init
from random import choice
import random
import os,pyfiglet
from colorama import Fore
import requests, re, sys, random, time, os, fontstyle
from colorama import Fore, Back, init
from threading import Thread

init(autoreset=True)
from random import choice

init()

black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'
all_col = [red, green, orange, cyan, lightred, lightgreen, yellow, lightcyan,lightblue,pink]
ran = random.choice(all_col)


def banner():
        os.system("clear")
        en = pyfiglet.figlet_format("Number\nGenerator\n")
        print(ran, en)
        print(ran + "\n\t\tV_2.5\t\n\n")

        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)


banner()


def exit():
    sys.exit()



l = [Style.BRIGHT + Fore.RED, Style.BRIGHT + Fore.LIGHTBLUE_EX, Style.BRIGHT + Fore.LIGHTCYAN_EX,
     Style.BRIGHT + Fore.LIGHTMAGENTA_EX, Style.BRIGHT + Fore.LIGHTYELLOW_EX, Fore.CYAN]

c = random.choice(l)
def randomcolors(n):

    c = random.choice(l)
    print(f"{c} {fontstyle.apply(n, 'bold')}")

def program():
    try:
        print('-' * 33)
        code = input(f'{c}Enter the Country Code [like +92 For Pakistan] : ')
        d = random.choice(l)
        print(d, '-' * 33)
        area_code = input(f'{d}Enter the Area Code [ Like 630 ] : ')
        e = random.choice(l)
        print('-' * 33)
        n = int(input(f"{e}Enter Amount of numbers: "))
        print(e, '-' * 33)
        f = random.choice(l)
        lent = int(input(f'{f}Length Remaining Digits [ 7 FOR USA ] : '))
        print(f, '-' * 33)
        mow = str('9' * lent)
        print(c, '-' * 33)

        def number_generator():
            first = str(random.randint(0, int(mow))).zfill(lent)
            return (first)

        j = random.choice(l)

        save = open('phone_numbers.txt', 'a+')
        for i in range(0, n):
            rez = code + area_code + number_generator()
            save.write(rez + '\n')
        print(f'{j}Phone Numbers Saved In phone_numbers.txt')





    except ValueError:
        print(f"{k}\nYou have missed something")


    except ModuleNotFoundError:
        os.system("pip install colorama")
        os.system("pip install fontstyle")
        os.system("pip install pyfiglet")

    except KeyboardInterrupt:
        randomcolors("\nHave a good ay :-)")

cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTGREEN_EX + "\n\n\t\t[1] Generate Numbers\n\t\t[2] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        program()

    elif choice == "2":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()














