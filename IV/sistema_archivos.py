# Crear clase para Inodos (archivos)
class Inodo:
    # Constructor
    def __init__(
        self, 
        tam, 
        fecha_creacion,
        fecha_modificacion,
        permisos,
        bloques):
        self.tam = tam
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
        self.permisos = permisos
        self.bloques = bloques

# Construir la clase de Bloques (Tamaño del archivo)
class Bloque:
    # Constructor
    def __init__(self, datos):
        self.datos = datos

# Construir Tabla para asignar bloques a inodos
class TablaAsignacionBloques:
    # Constructor
    def __init__(self):
        self.tabla = {}
    
    # Agregar los datos al archivo
    def asignar_bloque(self, inodo, bloque):
        self.tabla[inodo] = bloque
    
    # Obtener los datos del archivo
    def obtener_bloque(self, inodo):
        return self.tabla.get(inodo, None)

# Inodo + Bloques = Archivo

# Construir Acceso a los datos
class AccesoSecuencial:
    # Lectura de archivos
    def leer_archivo(self, archivo):
        with open(archivo, 'r') as f:
            datos = f.read()
        return datos
    # Escribir archivos
    def escribir_archivo(self, archivo, datos):
        with open(archivo, 'w') as f:
            f.write(datos)

# Construir lectura de archivos directa
class AccesoDirecto:
    # Lectura de archivos
    def leer_archivo(self, archivo, posicion):
        with open(archivo, 'r') as f:
            # Posicionarse en los datos
            # que se requieren
            f.seek(posicion)
            datos = f.read()
        return datos
    
    def escribir_archivo(self, archivo, datos, posicion):
        # Concatenar información al archivo
        with open(archivo, 'r+') as f:
            f.seek(posicion)
            f.write(datos)

class ListaEnlazada:
    # Constructor
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None


class InodoListaEnlazada(Inodo):
    # Constructor
    def __init__(self, 
                tam, 
                fecha_creacion, 
                fecha_modificacion,
                permisos,
                bloques):
        # Super = Manda llamar el constructor
        # de la clase Padre
        super().__init__(tam,
                        fecha_creacion,
                        fecha_modificacion,
                        permisos,
                        bloques)


class EntradaFAT:
    # Constructor
    def __init__(self, num_inodos, siguiente):
        self.num_inodos = num_inodos
        self.siguiente = siguiente


class FAT:
    # Constructor
    def __init__(self):
        self.entradas = {}
    
    def asignar_bloque(self, num_inodos, bloque):
        self.entradas[num_inodos] = bloque
    
    def obtener_bloque(self, num_inodos):
        return self.entradas.get(num_inodos, None)

# Método main
if __name__ == '__main__':
    # Crear un inodo (archivo vacío)
    inodo = Inodo(tam=1024, 
                fecha_creacion="2024-05-29",
                fecha_modificacion="2024-05-29",
                permisos="rw-",
                bloques=[1, 2, 3])
    
    # Creación de la tabla de asignaciones
    tabla = TablaAsignacionBloques()
    bloque1 = Bloque(datos='...')
    tabla.asignar_bloque(inodo, bloque1)
    bloque_asignado = tabla.obtener_bloque(inodo)
    
    # Acceder a los archivos de manera secuencial
    acceso_secuencial = AccesoSecuencial()
    datos_archivo = acceso_secuencial.leer_archivo("archivo.txt")
    print(datos_archivo)
    acceso_secuencial.escribir_archivo("archivo.txt", 
                                    "No es cierto, tqm Naylin.")
    
    # Acceder a los archivos de manera directa
    acceso_directo = AccesoDirecto()
    datos_archivo_directo = acceso_directo.leer_archivo("archivo.txt", 
                                                        posicion=18)
    print(datos_archivo_directo)
    acceso_directo.escribir_archivo("archivo.txt", 
                                    "Gloria", 
                                    posicion=18)