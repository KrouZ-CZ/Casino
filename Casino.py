
import os
import time
import math
import random
import colorama
from colorama import init
init()

#Титл
os.system("title Казино")
#Размер окна
os.system("mode con: cols=85 lines=12")
#Проверка файла с деньгами
os.system("if exist money.txt (echo 1) else (echo 100 >> money.txt)")

#Анимация Loading
def animate():
    from colorama import Fore, Back, Style
    os.system("cls")
    print("                                [+=          ]")
    print(" ")
    print("                                    " + Back.BLUE + "Loading" + Back.BLACK)
    print(" ")
    print("                                [+=          ]")
    time.sleep(0.5)
    os.system("cls")
    print("                                [+=+=        ]")
    print(" ")
    print("                                    " + Back.BLUE + "Loading" + Back.BLACK)
    print(" ")
    print("                                [+=+=        ]")
    time.sleep(0.5)
    os.system("cls")
    print("                                [+=+=+=      ]")
    print(" ")
    print("                                    " + Back.BLUE + "Loading" + Back.BLACK)
    print(" ")
    print("                                [+=+=+=      ]")
    time.sleep(0.5)
    os.system("cls")
    print("                                [  +=+=+=    ]")
    print(" ")
    print("                                    " + Back.BLUE + "Loading" + Back.BLACK)
    print(" ")
    print("                                [  +=+=+=    ]")
    time.sleep(0.5)
    os.system("cls")
    print("                                [    +=+=+=  ]")
    print(" ")
    print("                                    " + Back.BLUE + "Loading" + Back.BLACK)
    print(" ")
    print("                                [    +=+=+=  ]")
    time.sleep(0.5)
    os.system("cls")
    print("                                [      +=+=+=]")
    print(" ")
    print("                                    " + Back.BLUE + "Loading" + Back.BLACK)
    print(" ")
    print("                                [      +=+=+=]")
    time.sleep(0.5)
    os.system("cls")
    print("                                [        +=+=]")
    print(" ")
    print("                                    " + Back.BLUE + "Loading" + Back.BLACK)
    print(" ")
    print("                                [        +=+=]")
    time.sleep(0.5)
    os.system("cls")
    print("                                [          +=]")
    print(" ")
    print("                                    " + Back.BLUE + "Loading" + Back.BLACK)
    print(" ")
    print("                                [          +=]")
    time.sleep(0.5)
    os.system("cls")
#Проверка наличия денег на игру
def monpro(b):
    from colorama import Fore, Back, Style
    if int(b) < 10:
        os.system("cls")
        print(Fore.RED + "█▄░█ █▀█ ▀█▀   █▀▄▀█ █▀█ █▄░█ █▀▀ █▄█")
        print("█░▀█ █▄█ ░█░   █░▀░█ █▄█ █░▀█ ██▄ ░█░")
        input()
        os.system("exit")
    else:
        b = int(b) - 10
        return b
#Анализ выигрыша
def monkey(nb1, nb2, nb3):
    if nb1 == nb2:
        if nb2 == nb3:
            jackpot()
            return str(nb1) + str(0) + str(0)
        return str(nb1) + str(0)
    elif nb2 == nb3:
        return str(nb2) + str(0)
    elif nb1 == nb3:
        return str(nb1) + str(0)
    else:
        return 0
#Сохранение прогресса
def file(vm):
    file = open('money.txt')
    ba = file.read()
    file.close()
    bal = int(vm) + int(ba)
    w = open('money.txt', 'w')
    w.write(str(bal))
    w.close()
    return bal
#Джекпот!
def jackpot():
    from colorama import Fore, Back, Style
    print(Fore.WHITE + " ")
    time.sleep(5)
    print("           ░░░░░██╗░█████╗░░█████╗░██╗░░██╗██████╗░░█████╗░████████╗")
    print("           ░░░░░██║██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██╔══██╗╚══██╔══╝")
    print("           ░░░░░██║███████║██║░░╚═╝█████═╝░██████╔╝██║░░██║░░░██║░░░")
    print("           ██╗░░██║██╔══██║██║░░██╗██╔═██╗░██╔═══╝░██║░░██║░░░██║░░░")
    print("           ╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗██║░░░░░╚█████╔╝░░░██║░░░")
    print("           ░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░░░░╚═╝░░░")
#Меню)
def menu(bal):
    from colorama import Fore, Back, Style
    os.system("cls")
    print(Fore.WHITE + "                                                                 Баланс: " + str(bal) + "$")
    print("                  ░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░")
    print("                  ██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗")
    print("                  ██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║")
    print("                  ██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║")
    print("                  ╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝")
    print("                  ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░")
    vd = input(Fore.GREEN + "Нажми [enter] что-бы начать ")
    start(bal)
#Начало начал
def start(bal):
    bal = monpro(bal)
    from colorama import Fore, Back, Style
    #Генерация результатов
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    #n(1)2-это цифра n1(2)-это слой цифры 
    if num1 == 0:
        n11 = "####"
        n12 = "#  #"
        n13 = "#  #"
        n14 = "#  #"
        n15 = "####"
    if num1 == 1:
        n11 = "   #"
        n12 = "   #"
        n13 = "   #"
        n14 = "   #"
        n15 = "   #"
    if num1 == 2:
        n11 = "####"
        n12 = "   #"
        n13 = "####"
        n14 = "#   "
        n15 = "####"
    if num1 == 3:
        n11 = "####"
        n12 = "   #"
        n13 = " ###"
        n14 = "   #"
        n15 = "####"
    if num1 == 4:
        n11 = "#  #"
        n12 = "#  #"
        n13 = "####"
        n14 = "   #"
        n15 = "   #"
    if num1 == 5:
        n11 = "####"
        n12 = "#   "
        n13 = "####"
        n14 = "   #"
        n15 = "####"
    if num1 == 6:
        n11 = "####"
        n12 = "#   "
        n13 = "####"
        n14 = "#  #"
        n15 = "####"
    if num1 == 7:
        n11 = "####"
        n12 = "   #"
        n13 = "   #"
        n14 = "   #"
        n15 = "   #"
    if num1 == 8:
        n11 = "####"
        n12 = "#  #"
        n13 = "####"
        n14 = "#  #"
        n15 = "####"
    if num1 == 9:
        n11 = "####"
        n12 = "#  #"
        n13 = "####"
        n14 = "   #"
        n15 = "####"
    if num2 == 0:
        n21 = "####"
        n22 = "#  #"
        n23 = "#  #"
        n24 = "#  #"
        n25 = "####"
    if num2 == 1:
        n21 = "   #"
        n22 = "   #"
        n23 = "   #"
        n24 = "   #"
        n25 = "   #"
    if num2 == 2:
        n21 = "####"
        n22 = "   #"
        n23 = "####"
        n24 = "#   "
        n25 = "####"
    if num2 == 3:
        n21 = "####"
        n22 = "   #"
        n23 = " ###"
        n24 = "   #"
        n25 = "####"
    if num2 == 4:
        n21 = "#  #"
        n22 = "#  #"
        n23 = "####"
        n24 = "   #"
        n25 = "   #"
    if num2 == 5:
        n21 = "####"
        n22 = "#   "
        n23 = "####"
        n24 = "   #"
        n25 = "####"
    if num2 == 6:
        n21 = "####"
        n22 = "#   "
        n23 = "####"
        n24 = "#  #"
        n25 = "####"
    if num2 == 7:
        n21 = "####"
        n22 = "   #"
        n23 = "   #"
        n24 = "   #"
        n25 = "   #"
    if num2 == 8:
        n21 = "####"
        n22 = "#  #"
        n23 = "####"
        n24 = "#  #"
        n25 = "####"
    if num2 == 9:
        n21 = "####"
        n22 = "#  #"
        n23 = "####"
        n24 = "   #"
        n25 = "####"
    if num3 == 0:
        n31 = "####"
        n32 = "#  #"
        n33 = "#  #"
        n34 = "#  #"
        n35 = "####"
    if num3 == 1:
        n31 = "   #"
        n32 = "   #"
        n33 = "   #"
        n34 = "   #"
        n35 = "   #"
    if num3 == 2:
        n31 = "####"
        n32 = "   #"
        n33 = "####"
        n34 = "#   "
        n35 = "####"
    if num3 == 3:
        n31 = "####"
        n32 = "   #"
        n33 = " ###"
        n34 = "   #"
        n35 = "####"
    if num3 == 4:
        n31 = "#  #"
        n32 = "#  #"
        n33 = "####"
        n34 = "   #"
        n35 = "   #"
    if num3 == 5:
        n31 = "####"
        n32 = "#   "
        n33 = "####"
        n34 = "   #"
        n35 = "####"
    if num3 == 6:
        n31 = "####"
        n32 = "#   "
        n33 = "####"
        n34 = "#  #"
        n35 = "####"
    if num3 == 7:
        n31 = "####"
        n32 = "   #"
        n33 = "   #"
        n34 = "   #"
        n35 = "   #"
    if num3 == 8:
        n31 = "####"
        n32 = "#  #"
        n33 = "####"
        n34 = "#  #"
        n35 = "####"
    if num3 == 9:
        n31 = "####"
        n32 = "#  #"
        n33 = "####"
        n34 = "   #"
        n35 = "####"
    print(Fore.WHITE)
    #Переход на анимацию
    animate()
    print("                                  Вам выпало:")
    #Вывод результатов
    print(" ")
    print(Fore.MAGENTA + "                             +=+=+=+=+=+=+=+=+=+=")
    print(Fore.RED + "                              " + n11 + Fore.GREEN + "   " + n21 + Fore.CYAN + "   " + n31)
    print(Fore.RED + "                              " + n12 + Fore.GREEN + "   " + n22 + Fore.CYAN + "   " + n32)
    print(Fore.RED + "                              " + n13 + Fore.GREEN + "   " + n23 + Fore.CYAN + "   " + n33)
    print(Fore.RED + "                              " + n14 + Fore.GREEN + "   " + n24 + Fore.CYAN + "   " + n34)
    print(Fore.RED + "                              " + n15 + Fore.GREEN + "   " + n25 + Fore.CYAN + "   " + n35)
    print(Fore.MAGENTA + "                             +=+=+=+=+=+=+=+=+=+=")
    #Подсчёт выигрыша
    vigmon = monkey(num1, num2, num3)
    #Логи
    os.system("echo %date%  %time% @ Num: " + str(num1) + str(num2) + str(num3) + " Win: " + str(vigmon) + " Balance: " + str(bal) + " >> log.txt ")
    vg = int(vigmon) - 10
    print(" ")
    print(Fore.WHITE + "                                 Выигрыш: " + str(vg) + "$")
    #Перезапись баланса
    bal = file(str(vg))
    time.sleep(5)
    menu(bal)
#Начало
if __name__ == "__main__":
    b = open('money.txt', 'r')
    bal = b.read()
    b.close()
    menu(str(bal))
