import threading

def calcular_factorial(n, resultado):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    resultado.append(factorial)

if __name__ == "__main__":
    numero = 5
    resultados = []

    hilo_factorial = threading.Thread(target=calcular_factorial, args=(numero, resultados))
    hilo_factorial.start()
    hilo_factorial.join()

    resultado_hilos = resultados[0]
    print("Factorial con hilos de", numero, "es", resultado_hilos)
