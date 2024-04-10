import threading

# Crear un semáforo con un contador inicial de 1
semaphore = threading.Semaphore(1)

def worker(id):
    print(f"Worker {id} esperando el semáforo.")
    # Adquirir el semáforo
    semaphore.acquire()
    print(f"Worker {id} ha adquirido el semáforo.")
    # Realizar alguna tarea crítica
    print(f"Worker {id} realizando alguna tarea crítica.")
    # Liberar el semáforo
    semaphore.release()
    print(f"Worker {id} ha liberado el semáforo.")

# Crear varios hilos para ejecutar la función worker
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Esperar a que todos los hilos terminen
for t in threads:
    t.join()

print("Todos los hilos han terminado.")