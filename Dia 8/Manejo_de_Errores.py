def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)

#suma()

try:
    # Codigo que queremos probar
    suma()
except TypeError:
    #Codigo a ejecutar si no hay un error
    print("Estas intentando concatenar tipos de datos distintos")
except ValueError:
    #Codigo a ejecutar si no hay un error
    print("Eso no es un numero")
else:
    # Codigo a ejecutar siu no hay un error
    print("Hiciste todo bien")
finally:
    # COdigo que se va a ejecutar de todos modos
    print("Eso fue todo")

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")