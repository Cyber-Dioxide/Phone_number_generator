# Use With Python 3
import colorama

from fontstyle import apply
from colorama import Style , Fore
from phonenumbers.phonenumberutil import region_code_for_country_code
from pyfiglet import figlet_format
import requests, re, sys, random, time, os
from colorama import Fore, Back, init
from random import choice
import random
import os,pyfiglet
from colorama import Fore
import requests, re, sys, random, time, os, fontstyle
from threading import Thread

from random import choice



all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)


def banner():
        os.system("clear")

        print(ran, pyfiglet.figlet_format("\tNumber\nGenerator"))
        print(ran + "\n\t\tV_5.0.5 'Final Realese'\t\n\n")
        print("*" * 63)

        print(Style.BRIGHT+Fore.LIGHTCYAN_EX, "\n" ,"- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Style.BRIGHT+Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Style.BRIGHT+Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        print("\n" , "*" * 63)

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

        save = open('numbers.txt', 'a+')
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

def view():
    file = open("numbers.txt" , "r")
    print(ran , "\n\t\tThis is what i've found!\n")
    read = file.read()

    print(f"{ran} {read}")


cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTGREEN_EX + "\n\n\t\t[1] Generate Numbers\t\t\n\t\t[2] View Generated Numbers\n\t\t[3] Exit\n ")


    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        program()

    elif choice == "2":
        view()


    elif choice == "3":
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














