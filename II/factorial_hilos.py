import threading

def factorial(n, resultado):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    resultado.append(fact)

if __name__ == '__main__':
    numero = 50
    resultado = []
    
    # Creación hilo
    hilo = threading.Thread(target=factorial, args=(numero, resultado))
    hilo.start()
    hilo.join()
    
    resultado_final = resultado[0]
    print(f"El factorial de {numero} es {resultado_final}")