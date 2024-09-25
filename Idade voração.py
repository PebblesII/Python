idade = int(input("idade = "))

if idade < 16:
    print("Não pode votar")
elif idade >= 16 and idade < 18 or idade >= 70:
    print("opcional a votar")
else:
    print("Pode votar")


