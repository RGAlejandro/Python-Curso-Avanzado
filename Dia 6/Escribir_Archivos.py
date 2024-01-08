archivo = open("prueba1.txt", "w") #Si pones "a" no borra lo de arriba y escribes al final
archivo.write("Soy el nuevo texto")
archivo.writelines(["hola","mundo","aqui","estoy"])
archivo.close()