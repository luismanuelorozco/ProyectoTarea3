# Algoritmo para agregar marca de agua png a una imagen, proyecto simple para tarea 3 programacion 3 Luis Manuel Orozco 2019-8854

from PIL import Image
import os

# Ruta de la carpeta que contiene las imágenes
ruta_carpeta = r"C:\Users\LUIS\Desktop\PonerLogoYCambiarNombre"

# Ruta del archivo de la marca de agua
ruta_marca_de_agua = r"C:\Users\LUIS\Desktop\StrexPictures\Logos\LogoEsquinaBlancoVertical.png"

# Cargar la imagen de la marca de agua
marca_de_agua = Image.open(ruta_marca_de_agua)

# Recorrer la lista de archivos en la carpeta y aplicar la marca de agua a cada imagen
for nombre_archivo in os.listdir(ruta_carpeta):
    # Verificar si el archivo es una imagen
    if nombre_archivo.endswith(".jpg") or nombre_archivo.endswith(".png"):
        # Cargar la imagen principal
        imagen_principal = Image.open(os.path.join(ruta_carpeta, nombre_archivo))

        # Obtener el tamaño de la imagen principal
        ancho, alto = imagen_principal.size

        # Obtener el tamaño de la marca de agua
        marca_de_agua_ancho, marca_de_agua_alto = marca_de_agua.size

        # Calcular la posición de la marca de agua
        posicion_x = ancho - marca_de_agua_ancho
        posicion_y = alto - marca_de_agua_alto

        # Superponer la marca de agua en la imagen principal
        imagen_principal.paste(marca_de_agua, (posicion_x, posicion_y), marca_de_agua)

        # Guardar la imagen resultante
        imagen_principal.save(os.path.join(ruta_carpeta, nombre_archivo))
