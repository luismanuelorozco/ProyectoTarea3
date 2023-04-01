from PIL import Image
import os

# Ruta de la carpeta que contiene las imágenes
ruta_carpeta = r"C:\Users\LUIS\Desktop\PruebaCambioNombre"

# Recorrer la lista de archivos en la carpeta y recortar cada imagen
for nombre_archivo in os.listdir(ruta_carpeta):
    # Verificar si el archivo es una imagen
    if nombre_archivo.endswith(".jpg") or nombre_archivo.endswith(".png"):
        # Cargar la imagen
        imagen = Image.open(os.path.join(ruta_carpeta, nombre_archivo))

        # Obtener el tamaño de la imagen
        ancho, alto = imagen.size

        # Calcular el nuevo tamaño de la imagen con relación de aspecto 4:5
        nuevo_alto = alto
        nuevo_ancho = int(nuevo_alto * 4 / 5)

        # Calcular las coordenadas del cuadro de recorte
        x1 = (ancho - nuevo_ancho) // 2
        x2 = x1 + nuevo_ancho
        y1 = 0
        y2 = nuevo_alto

        # Recortar la imagen
        imagen_recortada = imagen.crop((x1, y1, x2, y2))

        # Guardar la imagen recortada
        imagen_recortada.save(os.path.join(ruta_carpeta, nombre_archivo))
