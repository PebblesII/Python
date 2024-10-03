import time
import sys
import os

os.system('cls||echo -e \\\\033c')

def Loading(timer):
    print("\n")
    for I in range(timer):
        print(".", end="")
        time.sleep(1)
    print("\n")

def LoadingPercen(Chegada, Pogress):
    Porcentagem = 0
    print("Começando Download", "-_" * 30)
    print("\n")
    while Porcentagem <= Chegada:
        if Porcentagem <= Chegada:
            print(f"\rDownload [%{Porcentagem}]", end="")
            Porcentagem += Pogress
            time.sleep(1)
            sys.stdout.flush()

#Boolean

Ligado = False

print("Ligar O Computador?")
print("    Y        N     ")
A = input("===    ")
if A == "Y":
    Ligado = True
elif A == "N":
    Ligado = False
    print("Turning off")
    Loading(3)
    os.system('cls||echo -e \\\\033c')
    exit()

else:
    print("Not valid Response, Exiting")
    Loading(3)
    os.system('cls||echo -e \\\\033c')
    exit()


print("-_" * 30)
print("Vereficando se Ligado")
print("-_" * 30)

Loading(3)

if Ligado:
    print("-_" * 30)
    print("Esta Ligado")
    print("-_" * 30)
else:
    print("-_" * 30)
    print("Não esta Ligado")
    print("-_" * 30)



Loading(3)

#Numeros


if Ligado:
    LoadingPercen(100, 10)

#Lists
print("\n" * 3)
ListNothing = []

ListGames = ["Minesweeper", "Purple place", "Snake"]

print(f"Games Installed\n")
for i in ListGames:
    print(f"{i}")
    print("--" * 30)
    time.sleep(1)

print("Any new Games?")
NewGame = input("=== ")



print("\n")
ListGames.append(NewGame)

print("-_" * 30)
print(f"{NewGame} Downloaded")
print("-_" * 30)


#Metodos de listas
#.append("Texto"), Adiciona algo ha lista
#.remove("Texto"), Remove algo da lista
#.pop[], Remove e retorna o valor removido



#Como Listas são chamadas
#LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#    [Start:   End:   How
#LIST[  1:      9:     3 ]
#print(LIST[1:9:3])
#Output = 3 6 9