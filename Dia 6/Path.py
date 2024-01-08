from pathlib import Path


base = Path.home()
guia = Path(base,"Barcelona","Sagrada_Familia.txt") #C:\Users\Alejandro\Barcelona\Sagrada_Familia
print(guia)
guia2 = guia.with_name("La_Pedrera.txt")
print(guia2)