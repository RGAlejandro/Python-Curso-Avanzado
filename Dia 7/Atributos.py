class Pajaro:

    alas = True

    def __init__(self,color, especie): #__init__ es la creacion del constructor
        self.color = color
        self.especie = especie
        #self se podria decir que es una representacion del objeto, como si fuese "this" en Java

mi_pajaro = Pajaro("rojo","loro")

print(mi_pajaro.color)
print(mi_pajaro.especie)

print(Pajaro.alas)
print(mi_pajaro.alas)
