def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x * 10

print(mi_funcion()) # si imprime el 4
print(mi_generador()) #no lo imprime ya que esta esperando a que se lo digas

g = mi_generador()
print(next(g))
print(next(g))