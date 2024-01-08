mi_archivo = open("prueba.txt")

#print(mi_archivo)  No te deja mostrarlo

print(mi_archivo.read()) # Asi si muestra el archivo txt

print(mi_archivo.readline()) # Solo lee una linea

print(mi_archivo.readlines()) # Lo guarda en una lista

mi_archivo.close() #Para cerrar el archivo al final b