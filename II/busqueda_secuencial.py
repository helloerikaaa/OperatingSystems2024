def buscar_elemento(lista, elemento):
    for i, val in enumerate(lista):
        if val == elemento:
            return i
    return -1

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elemento_a_buscar = 8
    indice_secuencial = buscar_elemento(lista, elemento_a_buscar)
    print("Índice secuencial de", elemento_a_buscar, "es", indice_secuencial)
