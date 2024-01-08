import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

patron = "ayuda"

busqueda = re.findall(patron, texto)
print(busqueda)

texto = "llama al 564-525-6588 ya mismo"

patron = r"\d\d\d-\d\d\d-\d\d\d\d"
patron = re.compile(r"\d{3}-\d{3}-\d{4}")

resultado = re.search(patron,texto)

print(resultado.group())


clave = input("Clave: ")
patron = r"\D{1}\w{7}"

chequear = re.search(patron,clave)


texto = "No atendemos los lunes por la tarde"

buscar = re.search(r"lunes|martes", texto)