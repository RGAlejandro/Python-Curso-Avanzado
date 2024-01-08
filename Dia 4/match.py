serie = "N-02"

'''if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe")'''
match serie:

    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe")


cliente = {"nombre": "Alejandro",
           "edad": 19,
           "ocupacion": "programador"}
pelicula = {"titulo": "Piratas del Caribe",
            "ficha_tecnica": {"protagonista": "Jack Sparoow",
                              "director": "Disney"}}
elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
            "director": director}}:
                print("Esto es una pelicula")
                print(titulo,protagonista,director)
        case _:
            print("No se que es esto")