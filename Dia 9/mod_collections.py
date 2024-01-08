from collections import Counter


numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]

print(Counter(numeros))

print(Counter("mississipi"))

serie = Counter([1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4])

print(serie.most_common())
print(serie.most_common(2)) # Muestra los 2 mas comunes
#Counter lo que hace es contar el numero de veces que sale tanto para arrays, como cadenas

from collections import defaultdict

#mi_dic = {"uno":"verde","dos":"azul","tres":"rojo"}
#print(mi_dic["cuatro"])

mi_dic = defaultdict(lambda: "nada")

mi_dic["uno"] = "verde"
print(mi_dic["dos"]) # Te pondra "nada" en lugar de salir error

from collections import namedtuple

Persona = namedtuple("Persona", ["nombre","altura","peso"])
ariel = Persona("Ariel", 1.76, 79)
print(ariel.altura) #De forma tradicional no te dejaria poner altura, tendrias que buscarlo por indice