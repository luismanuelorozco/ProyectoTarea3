# Algoritmo para reempalzar el nombre actual de una imagene por una secuencia de numeros deseada para asi establecer un orden, proyecto simple para tarea 3 programacion 3 Luis Manuel Orozco 2019-8854

import os

# Ruta de la carpeta que contiene las imágenes
ruta_carpeta = r"C:\Users\LUIS\Desktop\PonerLogoYCambiarNombre"

# Obtener la lista de archivos en la carpeta
lista_archivos = os.listdir(ruta_carpeta)

# Inicializar el contador para asignar el número secuencial
contador = 287

# Recorrer la lista de archivos y renombrar cada imagen
for nombre_archivo in lista_archivos:
    # Verificar si el archivo es una imagen
    if nombre_archivo.endswith(".jpg") or nombre_archivo.endswith(".png"):
        # Obtener la extensión del archivo
        extension = os.path.splitext(nombre_archivo)[1]
        # Construir el nuevo nombre de archivo con el número secuencial
        nuevo_nombre = str(contador) + extension
        # Renombrar el archivo
        os.rename(os.path.join(ruta_carpeta, nombre_archivo), os.path.join(ruta_carpeta, nuevo_nombre))
        # Incrementar el contador
        contador += 1
