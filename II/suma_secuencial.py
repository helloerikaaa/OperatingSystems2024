def calcular_suma(nums):
    suma_total = 0
    for num in nums:
        suma_total += num
    return suma_total

if __name__ == "__main__":
    # Lista de números
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Calcular la suma secuencialmente
    suma_secuencial = calcular_suma(numeros)
    print("Suma secuencial:", suma_secuencial)