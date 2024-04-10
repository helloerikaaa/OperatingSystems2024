import threading

def buscar_elemento(lista, elemento, inicio, fin, resultado):
    for i in range(inicio, fin):
        if lista[i] == elemento:
            resultado.append(i)

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elemento_a_buscar = 8
    resultados = []

    num_hilos = 4
    longitud_sublista = len(lista) // num_hilos

    hilos = []
    for i in range(num_hilos):
        inicio = i * longitud_sublista
        fin = (i + 1) * longitud_sublista if i < num_hilos - 1 else len(lista)
        hilo = threading.Thread(target=buscar_elemento, args=(lista, elemento_a_buscar, inicio, fin, resultados))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    indice_hilos = resultados[0] if resultados else -1
    print("Índice con hilos de", elemento_a_buscar, "es", indice_hilos)
