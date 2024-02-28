#!/bin/bash
# Comandos básicos para la navegación
echo "Listar contenido del directorio actual:"
ls
echo " "
echo "Cambiar al directorio anterior:"
cd ..
echo " "
echo "Mostrar la ruta del directorio actual:"
pwd
echo " "

# Creación y eliminación de directorios y archivos
echo "Crear un nuevo directorio llamado 'nuevo_directorio':"
mkdir nuevo_directorio
echo " "
echo "Eliminar el directorio 'nuevo_directorio':"
rmdir nuevo_directorio
echo " "
echo "Crear un nuevo archivo llamado 'nuevo_archivo.txt':"
touch nuevo_archivo.txt
echo " "
echo "Eliminar el archivo 'nuevo_archivo.txt':"
rm nuevo_archivo.txt
echo " "

# Copia, movimiento y renombrado de archivos y directorios
echo "Copiar el archivo 'archivo1.txt' a un nuevo archivo 'copia_archivo1.txt':"
cp archivo1.txt copia_archivo1.txt
echo " "
echo "Mover el archivo 'archivo2.txt' al directorio 'directorio_destino':"
mv archivo2.txt directorio_destino/
echo " "
echo "Renombrar el archivo 'viejo_nombre.txt' como 'nuevo_nombre.txt':"
mv viejo_nombre.txt nuevo_nombre.txt
echo " "

# Visualización de contenido de archivos
echo "Mostrar el contenido completo del archivo 'archivo.txt':"
cat archivo.txt
echo " "
echo "Mostrar las primeras 10 líneas del archivo 'archivo.txt':"
head archivo.txt
echo " "
echo "Mostrar las últimas 10 líneas del archivo 'archivo.txt':"
tail archivo.txt
echo " "

# Búsqueda de archivos
echo "Buscar archivos con extensión '.txt' en el directorio actual y sus subdirectorios:"
find . -name "*.txt"
echo " "
echo "Buscar la palabra 'ejemplo' en el archivo 'archivo.txt':"
grep "ejemplo" archivo.txt
echo " "

# Agregar una línea al archivo.txt
echo "Agregando una nueva línea al archivo 'archivo.txt':"
echo "Esta es una nueva línea" >> archivo.txt
