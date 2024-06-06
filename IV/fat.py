class File:
    # Constructor
    def __init__(self, nombre, tam):
        self.nombre = nombre
        self.tam = tam
        # Archivo vacío
        self.datos = None

# Sistema FAT
class FAT:
    # Constructor
    def __init__(self, tam_disco):
        self.tam_disco = tam_disco
        self.espacio_libre = tam_disco
        self.fat = {}
        self.archivos = {}
    
    def crear_archivo(self, nombre, tam):
        # Verificar que existe espacio libre
        if tam > self.espacio_libre:
            print("Ya no hay espacio disponible :(")
            return
        # Crear el archivo
        self.archivos[nombre] = File(nombre, tam)
        # Pasar el archivo al sistema FAT bit por bit
        self.fat[nombre] = [i for i in range(tam)]
        # Actualizar el espacio disponible
        self.espacio_libre -= tam
        print(f"El archivo {nombre} se ha creado con un tamaño {tam}")
    
    def borrar_archivo(self, nombre):
        if nombre in self.archivos:
            # Obtener el tamaño del archivo
            tam = self.archivos[nombre].tam
            # Eliminar el archivo
            del self.archivos[nombre]
            del self.fat[nombre]
            # Actualizar el espacio libre
            self.espacio_libre += tam
            print(f"El archivo {nombre} se eliminó")
        else:
            print("No se encontró el archivo")


if __name__ == '__main__':
    # Instancia del sistema FAT
    fat = FAT(100)
    # Crear archivos
    fat.crear_archivo("archivo1.txt", 30)
    fat.crear_archivo("archivo2.txt", 80)
    fat.crear_archivo("archivo3.txt", 50)
    # Eliminar archivos
    fat.borrar_archivo("archivo1.txt")
    fat.borrar_archivo("archivo5.txt")
