def calcular_suma(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

if __name__ == '__main__':
    #numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numeros = [x for x in range(100000000)]
    suma = calcular_suma(numeros)
    print(f'La suma es {suma}')
