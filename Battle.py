import time
import os
from typing import final


def logo():
    print("██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗")
    print("██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝")
    print("██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░")
    print("██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░")
    print("██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗")
    print("╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝")


def clear():
    os.system('cls||echo -e \\\\033c')

#Loadings
def Loading(timer, times):
    for x in range(times):
        for I in range(timer):
            print(".", end="")
            time.sleep(0)
        print(f"\r   ", end="")
        print("\r", end="")

#Text Handler

def TextHandler(Texto):
    for i in Texto:
        print(i, end="")
        time.sleep(0)
    print("\n")

TextHandler("Would you like to start?")

TextHandler("   YES    or    NO    ")

Answer = input("Answear = ")
Yes = ["yes", "y", "Y", "Yes", "YEs", "YES"]
No = ["no", "n", "N", "No"]

if Answer in Yes:
    clear()
    TextHandler("Starting")
    Loading(3, 2)
elif Answer in No:
    clear()
    TextHandler("Quitting")
    Loading(3, 2)
    quit()
else:
    print("Error")
    quit()

clear()
logo()

#Creating Char
print("\n")
TextHandler("Create a new Character")
CharName = input(" ")

clear()
print(f"Creating {CharName}")
Loading(3, 3)


#Char Status
Charstatus = {
    "Health": 0,
    "Attack": 0,
    "Agility": 0,
    "Defense": 0

}
CharXP = 0
CharHP = 100
CharATK = 10
CharAGY = 30
CharDefense = 5

clear()

def Callstatus():
    print(Charstatus)
    print("     1             2           3            4       ")

def LevelUp(Points):
    while Points > 0:
        Choice = int(input(""))
        if Choice == 1:
            Charstatus["Health"] += 1
            Callstatus()
            print(f"Health Increased {CharHP}")
            Points -= 1
        if Choice == 2:
            Charstatus["Attack"] += 1
            Callstatus()
            Points -= 1
        if Choice == 3:
            Charstatus["Agility"] += 1
            Callstatus()
            Points -= 1
        if Choice == 4:
            Charstatus["Defense"] += 1
            Callstatus()
            Points -= 1
    print(f"Points = {Points}")


print(f"{CharName} Status")
Callstatus()


print(f"You have 3 Points What do you want to level up")
LevelUp(3)

#GameplayLoop

def battle(situation):
    if situation == 1:
        EnemyH = 30
        EnemyATK = 10
    
