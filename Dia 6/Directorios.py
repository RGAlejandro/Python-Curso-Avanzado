import os

ruta = os.getcwd() #obtener ruta actual

ruta = os.chdir("C:\\Users\\Alejandro\\Documents\\Python\\Alternativo")

#ruta = os.makedirs("C:\\Users\\Alejandro\\Documents\\Python\\Alternativo\\otra") crear carpeta

#ruta = os.rmdir("C:\\Users\\Alejandro\\Documents\\Python\\Alternativo\\otra") Eliminar carpeta
archivo = open("otroarchivo.txt")
print(archivo.read())


#FORMA UNIVERSAL TANTO WINDOWS COMO LINUX

from pathlib import Path

carpeta = Path("C:/Users/Alejandro/Documents/Python/Alternativo")
archivo = carpeta / "otroarchivo.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())