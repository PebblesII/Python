import time
import sys

#Boolean

Habilitado = True

I = 2
print("-_" * 30)
print("Vereficando se Habilitado")
print("-_" * 30)
print("\n")

while I >= 0:
    print(".", end="")
    time.sleep(1)
    I -= 1

print("\n")

if Habilitado:
    print("-_" * 30)
    print("Esta Habilitado")
    print("-_" * 30)
    print("\n" * 3)
else:
    print("-_" * 30)
    print("Não esta Habilitado")
    print("-_" * 30)
    print("\n" * 3)


#Numeros

Chegada = 100
Porcentagem = 0
if Habilitado:
    print("Começando Download", "-_" * 30)
    print("\n")
    while Porcentagem <= Chegada:
        if Porcentagem <= Chegada:
            print(f"\rDownload [%{Porcentagem}]", end="")
            Porcentagem += 10
            time.sleep(1)
            sys.stdout.flush()

#Lists
print("\n" * 3)
ListNothing = []

ListGames = ["Minesweeper", "Purple place", "Snake"]

print(f"Games Installed\n")
for i in ListGames:
    print(f"{i}")
    print("--" * 30)
    time.sleep(1)

#Como Listas são chamadas

#    [Start:   End:   How
#LIST[  1:      9:     3 ]
#print(LIST[1:9:3])
#Output = 3 6 9

