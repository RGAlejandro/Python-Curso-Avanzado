from pathlib import Path, PureWindowsPath

# Asi no necesitas hacer el open ni el close

carpeta = Path("C:/Users/Alejandro/Documents/Python/Dia 6/prueba.txt")
ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)

print(carpeta.read_text())

print(carpeta.stem) #devuelve prueba
print(carpeta.suffix) # devuelte que es un .txt

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Este archivo si existe")
