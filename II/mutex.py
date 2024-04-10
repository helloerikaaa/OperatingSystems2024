import threading

# Clase que implementa un Mutex utilizando un semáforo
class Mutex:
    def __init__(self):
        # Crear un semáforo con un contador inicial de 1
        self.semaphore = threading.Semaphore(1)

    # Método para adquirir el mutex
    def acquire(self):
        self.semaphore.acquire()

    # Método para liberar el mutex
    def release(self):
        self.semaphore.release()

# Crear una instancia de Mutex
mutex = Mutex()

# Función que será ejecutada por cada hilo
def worker(id):
    print(f"Worker {id} esperando el mutex.")
    # Adquirir el mutex
    mutex.acquire()
    print(f"Worker {id} ha adquirido el mutex.")
    # Realizar alguna tarea crítica
    print(f"Worker {id} realizando alguna tarea crítica.")
    # Liberar el mutex
    mutex.release()
    print(f"Worker {id} ha liberado el mutex.")

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