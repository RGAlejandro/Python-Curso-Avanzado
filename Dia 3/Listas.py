mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista+mi_lista2

mi_lista3[0] = "Ale"

mi_lista3.append("g")#Agrega un elemento a la lista
eliminado = mi_lista3.pop(0)#Elimina el ultimo

print(mi_lista3)
print(eliminado)

print(mi_lista3)
otra_lista=['hola',55,6.1]
resultado = len(mi_lista)
print(resultado)
resultado2 = mi_lista[0]
print(resultado2)
resultado3 = mi_lista[0:2]
print(resultado3 )


print(type(mi_lista))


#ORDENAR
lista = ["g","o","b","m","c"]
nueva_lista = lista.sort() #NO TE DEJA GUARDARLO EN UNA VARIABLE YA QUE NO SE ALMACENA LA INFORMACION
lista.sort()
print(lista)
lista.reverse() # ORDENACION INVERSA
print(lista)