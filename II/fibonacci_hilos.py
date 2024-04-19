import threading

def fibo(n):
    # Casos base
    if n <=1:
        return n
    else:
        # Caso general
        return fibo(n-1) + fibo(n-2)

def calcular_fibo_con_hilos(limite):
    fibonacci = []
    # Anidar una función para calcular el limite
    def calcular_rango(inicio, fin):
        for i in range(inicio, fin):
            fibonacci.append(fibo(i))

    num_hilos = 2
    # Arreglo para enlistar todos los hilos
    hilos = []
    
    # Calcular cuántos número va a ejecutar cada hilo
    terminos_por_hilo = limite // num_hilos
    
    # Crear y ejecutar los hilos
    for i in range(num_hilos):
        inicio = i * terminos_por_hilo
        fin = (i+1) * terminos_por_hilo if i < num_hilos -1 else limite
        
        # Crear el hilo
        hilo = threading.Thread(target=calcular_rango, 
                                args=(inicio, fin))
        # Agregar el hilo a lista
        hilos.append(hilo)
        # Ejecutar el hilo
        hilo.start()
    
    # Esperar a que los hilos terminen 
    # y mostrar el resultado final
    for hilo in hilos:
        hilo.join()

    return fibonacci

if __name__ == '__main__':
    n = 40 
    f = calcular_fibo_con_hilos(n)
    print(f"La secuencia fibonacci para n = {n} es {f}")