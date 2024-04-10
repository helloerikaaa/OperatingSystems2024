def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    numero = 5
    resultado_secuencial = factorial(numero)
    print("Factorial secuencial de", numero, "es", resultado_secuencial)
