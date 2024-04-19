# importar el paquete para manejar hilos
import threading

def calcular_suma(numeros, inicio, fin, resultado):
    # Resultado de la suma de la sublista
    suma_parcial = 0
    for i in range(inicio, fin):
        suma_parcial += numeros[i]
    resultado.append(suma_parcial)

if __name__ == '__main__':
    #numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numeros = [x for x in range(100000000)]
    num_hilos = 4
    # Calcular la cantidad de sublistas
    len_sublistas = len(numeros) // num_hilos
    
    # Lista para guardar los resultados
    resultados = []
    # Lista para guardar los hilos
    hilos = []
    for i in range(num_hilos):
        inicio = i * len_sublistas
        fin = (i + 1) * len_sublistas if i < num_hilos - 1 else len(numeros)
        
        # Crear el hilo
        hilo = threading.Thread(target=calcular_suma, args=(numeros, inicio, fin, resultados))
        # Agregar el hilo a la lista
        hilos.append(hilo)
        # Ejecutamos el hilo
        hilo.start()
    
    # Esperar que los hilos terminen su trabajo
    for hilo in hilos:
        hilo.join()
    
    # El resultado de la suma de los números
    suma_total = sum(resultados)
    print(f"La suma con hilos es {suma_total}")
