# Algoritmo LRU (Least Recently Used)
# La página que no ha sido accedida durante más tiempo
from collections import OrderedDict

class LRU:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        # Ordenar los procesos según su utilización
        self.cache = OrderedDict()
    
    def crear_paginacion(self, pagina):
        # Si la página ya está en memoria
        # Se actualiza el tiempo de acceso
        if pagina in self.cache:
            self.cache.move_to_end(pagina)
        # Si no está en memoria
        # Se elimina el más antiguo
        else:
            if len(self.cache) >= self.capacidad:
                self.cache.popitem(last=False)
                # Eliminar la página menos 
                # recientemente utilizada
            self.cache[pagina] = True
    
    def imprimir_paginacion(self):
        print(f"Páginas en memoria {list(self.cache.keys())}")

if __name__ == '__main__':
    # Instancia del algoritmo
    lru = LRU(3)
    
    # Secuencia de páginas
    paginas = [1, 2, 3, 4, 1, 2]
    
    # Simulación de asignación de páginas
    for pagina in paginas:
        lru.crear_paginacion(pagina)
        lru.imprimir_paginacion()