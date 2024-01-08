palabra = "python"

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

lista = [letra for letra in palabra]

lista = [n/2 for n in range(0,21,2)]


lista = [n for n in range(0,21,2)if n * 2 > 10]

lista = [n if n * 2 > 10 else "no" for n in range(0,21,2)]


pies = [10,20,30,40,50]
metros = [round((p / 3.281),2) for p in pies]

print(metros)
