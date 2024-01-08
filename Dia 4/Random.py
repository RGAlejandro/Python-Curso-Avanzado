from random import *

aleatorio = randint(1,5) #Se incluyen ambos parametros
print(aleatorio)

aleatorio = round(uniform(1,5),1) #Numeros decimales

aleatorio = random() # Entre 0 y 1

colores = ["azul","amarillo","rojo","verde"]

aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))

shuffle(numeros) # Cambia el orden de las posiciones

print(numeros)