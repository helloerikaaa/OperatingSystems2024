# Algoritmo FIFO (First In, First Out)

class FIFO:
    def __init__(self, capacidad):
        # Capacidad de la cola
        self.capacidad = capacidad
        # Instancia de la cola
        self.cola = []
    
    def crear_paginacion(self, pagina):
        # Comprobar que hay espacio en la cola
        if len(self.cola) < self.capacidad:
            self.cola.append(pagina)
        # si la capacidad está llena
        # se elimina la página más vieja
        else:
            # Eliminando la página más vieja
            self.cola.pop(0)
            # Agregar la nueva página (push)
            self.cola.append(pagina)
    
    # Imprimir tabla de paginación
    def imprimir_paginacion(self):
        print(f"Páginas en memoria {self.cola}")

if __name__ == '__main__':
    # Instancia de mi algoritmo FIFO
    fifo = FIFO(3)
    
    # Secuencia de páginas
    paginas = [1, 2, 3, 4, 1, 2]
    
    # Simulación de páginas en la tabla
    for pagina in paginas:
        fifo.crear_paginacion(pagina)
        fifo.imprimir_paginacion()