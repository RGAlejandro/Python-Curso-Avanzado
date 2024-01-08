nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42,55] #Se puede añadir mas, pero solo llegara hasta el limite de la lista corta
ciudades = ["Madrid","Lima","Mexico"]

combinados = list(zip(nombres,edades,ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")