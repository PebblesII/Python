import time
import os

def logo():
    print("▒█▀▄▀█ ▀█▀ ▒█▄░▒█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▀▀ ▀▀█▀▀")
    print("▒█▒█▒█ ▒█░ ▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█▄▄▀ ▒█▄▄█ ▒█▀▀▀ ░▒█░░")
    print("▒█░░▒█ ▄█▄ ▒█░░▀█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█░░░ ░▒█░░")


def clear():
    os.system('cls||echo -e \\\\033c')

#Loadings
def Loading(timer, times):
    print("\n")
    for x in range(times):
        for I in range(timer):
            print(".", end="")
            time.sleep(1)
        print(f"\r   ", end="")
        print("\r", end="")

#Text Handler

def TextHandler(Texto):
    for i in Texto:
        print(i, end="")
        time.sleep(.1)
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
print("\n")
TextHandler("Create new world")
WorldName = input(" ")
