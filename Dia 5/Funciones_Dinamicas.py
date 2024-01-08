def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado)

def chequear_lista_numeros(lista):
    '''
    Esto mirara en una lista si existe algun numero que tenga 3 cifras
    '''
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass #Si pusiera False entonces a la que encuentre un numero que no sea de 3 cifras mostrara siempre False
    return False

resultado = chequear_lista_numeros([3,33,333,3333])
print((resultado))

def obtener_numeros_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

listaNumeros = obtener_numeros_3_cifras([555,99,666])
print(listaNumeros)