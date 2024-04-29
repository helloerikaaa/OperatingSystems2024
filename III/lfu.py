# LFU (Least Frequently Used)
from collections import defaultdict

class LFU:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = {}
        self.frecuencia = defaultdict(int)
    
    def crear_paginacion(self, pagina):
        # Si la página ya existe en la tabla
        if pagina in self.cache:
            # incrementar el contador de visitas
            self.frecuencia[pagina] += 1
        else:
            # Verificar que el caché no sea
            # mayor a la capacidad de la tabla
            if len(self.cache) >= self.capacidad:
                menor = min(self.frecuencia, key=self.frecuencia.get)
                # Se elimina la página de la tabla
                del self.cache[menor]
                # Se elimina la frecuencia de esa página
                del self.frecuencia[menor]
            self.cache[pagina] = True
            self.frecuencia = 1
    
    def imprimir_paginacion(self):
        print(f"Páginas en memoria {self.cache.keys()}")

if __name__ == '__main__':
    lfu = LFU(3)
    paginas = [1, 2, 3, 4, 1, 2]
    
    # Simulación de paginación
    for pagina in paginas:
        lfu.crear_paginacion(pagina)
        lfu.imprimir_paginacion()
