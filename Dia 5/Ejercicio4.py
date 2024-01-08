def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(numero):
    cantidad_primos = 0
    print(f"Números primos en el rango de 2 a {numero}:")
    for i in range(2, numero + 1):
        if es_primo(i):
            print(i)
            cantidad_primos += 1
    return cantidad_primos

numero_proveedor = 20
cantidad = contar_primos(numero_proveedor)
print(f"\nEncontrados {cantidad} números primos en el rango de 2 a {numero_proveedor}.")
