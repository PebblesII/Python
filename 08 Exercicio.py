def contador(ano):
    meses = ano * 12
    dias = meses * 30
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60
    print(f"{ano} Anos equivale ha= {meses} Meses, {dias} Dias, {horas} Horas, {minutos} Minutos, {segundos} Segundos")

Quantidade = int(input("Quantidade de anos = "))
contador(Quantidade)
