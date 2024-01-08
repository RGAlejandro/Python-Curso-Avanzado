nombre = input("Indique su nombre ")
ventas = int(input("Indica las ventas que has tenido "))

dineroRedondeado = round(ventas * 0.13)
print(f"Hola {nombre}, has ganado un total de {dineroRedondeado}€")