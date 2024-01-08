#Primero introducir un texto
texto = input("Introduzca un texto para analizarlo ")
letra1 = input("Introduzca la primera letra ")
letra2 = input("Introduzca la segunda letra ")
letra3 = input("Introduzca la tercera letra ")
primeraLetra = texto[0]
ultimaLetra =  texto [-1]
texto = texto.lower()
print(texto)
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

resultado1 = texto.count(letra1)
resultado2 = texto.count(letra2)
resultado3 = texto.count(letra3)

lista_num_veces = [resultado1,resultado2,resultado3]


print("1.- Cada letra aparece este numero de veces")
print(lista_num_veces)

palabras = texto.split(" ")  # Ahora es una lista
contarPalabras = len(palabras)

print(f"2.- La siguiente frase tiene un total de {contarPalabras} palabras")
print("3.- La primera y ultima letra es ")
print(f"3.- La primera es {primeraLetra} y ultima letra es {ultimaLetra}")
print("4.- Las palabras en orden inverso quedaria asi ")
palabras.reverse()
reverso = " ".join(palabras)
print(reverso)
print("5-¿Aparece python dentro del texto?")
aparece = "python" in texto
dic = {True:"si",False:"no"}
print(f"La palabra 'Python' {dic[aparece]} se encuentra en el texto")
print(aparece)

