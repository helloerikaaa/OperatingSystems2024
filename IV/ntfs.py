class File:
    # Constructor
    def __init__(self, nombre, tam, permisos):
        self.nombre = nombre
        self.tam = tam
        # Archivo vacío
        self.datos = None
        self.permisos = permisos


# Sistema NTFS (New Technology File System)
class NTFS:
    # Constructor
    def __init__(self):
        self.archivos = {}
        self.bitacora = []
        
    def crear_archivo(self, nombre, tam, permisos):
        self.archivos[nombre] = File(nombre, tam, permisos)
        # Se guarda el historial de los archivos
        self.bitacora.append(
            f"El archivo {nombre} con tamaño {tam} \
            se ha creado con los permisos {permisos}")
        print(f"El archivo {nombre} con tamaño {tam} \
            se ha creado con los permisos {permisos}")
    
    def borrar_archivo(self, nombre):
        # Verificar que el archivo esté en el sistema
        if nombre in self.archivos:
            del self.archivos[nombre]
            self.bitacora.append(f"Se borró el archivo {nombre}")
            print("Se borró el archivo")
        else:
            print("No se encontró el archivo")


if __name__ == '__main__':
    # Instancia del sistema de archivos
    ntfs = NTFS()
    # Crear archivos
    ntfs.crear_archivo("archivo.txt", 40000, "r")
    ntfs.crear_archivo("archivo1.txt", 10, "rw")
    # Borrar archivos
    ntfs.borrar_archivo("archivo.txt")
