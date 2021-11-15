#Use With Python 3
import colorama
from fontstyle import apply
from colorama.ansi import Style
from phonenumbers.phonenumberutil import region_code_for_country_code
from pyfiglet import figlet_format
import requests,re,sys,random,time,os
from colorama import Fore, Back, init
from random import choice
import random
import os
from colorama import Fore
import requests,re,sys,random,time,os,fontstyle
from colorama import Fore, Back, init
from threading import Thread
init (autoreset = True)
from random import choice
init()

os.system('cls')

y= """ 

                     Phone Number Generator   
                      
                                [+] My Instagram: @saadkhan041 , @coding_memz      [+]
                                [+]Author: Saad Khan             [+]
                                
                                
                                          
                              +-------- With Great Power Comes Great Toolz! --------+

			                  """

l = [Style.BRIGHT+Fore.RED, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX,Fore.CYAN]
def randomcolors(n):
        c = random.choice(l)
        print(f"{c} {fontstyle.apply(n, 'bold')}")

phone = figlet_format("Phone")
num = figlet_format("Number")
gen = figlet_format("Generator")
print(fontstyle.apply(figlet_format("Phone\nNumber\nGenerator") , "light green/bold"))
c = random.choice(l)
print(fontstyle.apply(y , "cyan/bold"))
k = random.choice(l)
def program():
    try:
        print('-'*33)
        code = input(f'{c}Enter the Country Code [like +92 For Pakistan] : ')
        d = random.choice(l)
        print(d,'-'*33)
        area_code = input(f'{d}Enter the Area Code [ Like 630 ] : ')
        e = random.choice(l)
        print('-'*33)
        n = int(input(f"{e}Enter Amount of numbers: "))
        print(e,'-'*33)
        f = random.choice(l)
        lent = int(input(f'{f}Length Remaining Digits [ 7 FOR USA ] : '))
        print(f,'-'*33)
        mow = str('9'*lent)
        print(c,'-'*33)
        def number_generator():
            first = str(random.randint(0,int(mow))).zfill(lent)
            return (first)

        j = random.choice(l)

        save = open('Phone_Numbers.txt','a+')
        for i in range(0,n):
            rez = code+area_code+number_generator()
            save.write(rez + '\n')
        print(f'{j}Phone Numbers Saved In Phone_Numbers.txt')
    
        

    

    except ValueError:
        print(f"{k}You have missed something")
        exit

    except ModuleNotFoundError:
        os.system("pip install colorama")

    except ModuleNotFoundError:
        os.system("pip install fontstyle")
    
    except KeyboardInterrupt:
        randomcolors("Have a good ay :-)")
        exit
    
    
con = "" 
while con != "n" and "no":
    program()
      

    con=input(f'{k}Do you want to continue? [y/n]: ')
    
    if con == "n":
        break
    elif con =="no":
        break

    
    

   

            

    

    


