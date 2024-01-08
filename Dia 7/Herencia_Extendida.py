class Padre:
    def hablar(self):
        print("Hola")

class Madre:

    def reir(self):
        print("jajaja")
    def hablar(self):
        print("que tal")

class Hijo(Madre,Padre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

print(Nieto.__mro__)