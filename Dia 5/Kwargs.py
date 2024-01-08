def suma(**kwargs):
    total = 0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    print(type(kwargs))
    return total

total = suma(x=3, y=5,z=2)
print(total)


def prueba(num1,num2,*args,**kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")


    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

    return total

prueba(15,50,100,200,300,400,x="uno",y="dos",z="tres")