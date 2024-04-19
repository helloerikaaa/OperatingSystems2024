def factorial(n):
    # Guardar el resultado final
    fact = 1
    # Rango de 1 a n
    for i in range(1, n+1):
        # Calcular el factorial
        fact *= i
    return fact

# Ejecutar la función
if __name__ == "__main__":
    numero = 50
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")