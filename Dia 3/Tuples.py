mi_tuple = (1,2,3,4) #Se puede hacer con o sin parentesis, luego no se modifica su contenido

print(mi_tuple[0])


mi_tuple2 = (1,2,(10,20),4)
print(mi_tuple2[2][0])

mi_tuple = list(mi_tuple) #Con esto se pasa de tuple a lista, de esa forma ya se podria editar o agregar
mi_tuple = tuple(mi_tuple) # Asi se convierte de nuevo a tuple

t = (1,2,3)
x,y,z = t #Tiene que haber la misma cantidad de elementos o sino dará error
print(x,y,z)

t2 = (1,2,3,1)
print(len(t2)) #daria 4
print(t2.count(1)) #cuantas veces sale ese elemento