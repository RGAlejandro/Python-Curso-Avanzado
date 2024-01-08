


#def una_funcion(funcion):
    #return funcion

#una_funcion(mayuscula("probando"))

def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula



def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion


def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula("alejandro")
mayuscula_decorada("alejandro")