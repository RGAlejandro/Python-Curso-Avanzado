lista = ["a","b","c","d"]

for letra in lista:
    numero_letra=lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista2 = ["pablo","laura","fede","luis","julia"]
for nombre in lista2:
    if nombre.startswith("l"): #Esta condicion dice que el nombre tiene que empezar por l
        print(nombre)
    else:
        print("Nombre que no comienza con L")

numeros = [1,2,3,4,5]
mi_valor=0

for numero in numeros:
    mi_valor=mi_valor+numero

print(mi_valor)

palabra="python"

for letra in palabra:
    print(letra)

dic = {"clave1":"a","clave2":"b","clave3":"c"}

for a,b in dic.items():
    print(a,b)