from random import *

nombre = input("Como te llamas ")

#print(f"Te llamas {nombre}")

numeroSecreto = randint(1,100)

#print(numeroSecreto)

intentos = 8

for _ in range(intentos):
    if intentos < 1:
        print(f"Lo siento {nombre} pero no has encontrado el numero secreto")
        break
    print(f"Llevas {8-intentos} intentos {nombre}, te quedan {intentos} oportunidades para adivinar el numero. ")
    numElegir = int(input("Introduce un numero para averiguar si es el numero secreto "))

    if numElegir < numeroSecreto:
        print("El numero secreto es mas alto que tu numero elegido")
        intentos -= 1
    if numElegir > numeroSecreto:
        print("El numero secreto es mas bajo que tu numero elegido")
        intentos -= 1
    if numElegir == numeroSecreto:
        print(f"Enhorabuena, encontraste el numero secreto {numeroSecreto}")
        break

if intentos == 0:
    print(f"Lamento que hayas perdido el juego {nombre}, vuelve a jugar cuando tengas ganas")
else:
    print(f"WOW, ERES MUY BUENO {nombre}, TIENES MIS RESPETOS")