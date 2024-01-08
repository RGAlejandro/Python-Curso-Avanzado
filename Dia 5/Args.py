def suma (a,b):
    return a + b

print(suma(5,6))

def sumaInfinito(*args):
    total = 0
    for arg in args:
        total += arg
    return total
