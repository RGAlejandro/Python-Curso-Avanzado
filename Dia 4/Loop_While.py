monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas-=1
else:
    print("No tengo más dinero")

respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

respuesta = "s"

while respuesta == "s":
    pass

nombre = input("introduce tu nombre")

for letra in nombre:
    if letra == "r":
        break #Federico solo pondria Fede con continue seria Fedeico
    print(letra)