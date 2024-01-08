def cero_repetido_dos_veces_consecutivas(*numeros):
    for i in range(len(numeros) - 1):
        if numeros[i] == 0 and numeros[i + 1] == 0:
            return True
    return False