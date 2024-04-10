import threading

def calcular_suma(nums, inicio, fin, resultado):
    suma_parcial = 0
    for i in range(inicio, fin):
        suma_parcial += nums[i]
    resultado.append(suma_parcial)

if __name__ == "__main__":
    # Lista de números
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Número de hilos
    num_hilos = 4
    # Dividir la lista en partes iguales para cada hilo
    longitud_sublista = len(numeros) // num_hilos

    # Lista para almacenar los resultados parciales
    resultados = []

    # Crear y lanzar los hilos
    hilos = []
    for i in range(num_hilos):
        inicio = i * longitud_sublista
        fin = (i + 1) * longitud_sublista if i < num_hilos - 1 else len(numeros)
        hilo = threading.Thread(target=calcular_suma, args=(numeros, inicio, fin, resultados))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Calcular la suma total a partir de los resultados parciales
    suma_total = sum(resultados)
    print("Suma con hilos:", suma_total)
