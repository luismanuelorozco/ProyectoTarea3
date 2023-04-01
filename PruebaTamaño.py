from PIL import Image
import os

# establecer el tamaño y relación de aspecto deseada
width = 1080
height = 1350

# establecer la ruta de la carpeta con las imágenes originales
input_folder = r"C:\Users\LUIS\Desktop\PruebaCambioNombre"

# establecer la ruta de la carpeta donde se guardarán las imágenes redimensionadas
output_folder = r"C:\Users\LUIS\Desktop\PruebaCambioNombre\Redimensionadas"

# recorrer cada archivo en la carpeta de entrada
for filename in os.listdir(input_folder):
    filepath = os.path.join(input_folder, filename)

    # abrir la imagen y obtener su tamaño original
    with Image.open(filepath) as img:
        original_width, original_height = img.size

        # calcular el tamaño nuevo para mantener la relación de aspecto
        new_width = int(original_height * aspect_ratio)
        new_height = original_height

        # si el nuevo tamaño excede el ancho deseado, ajustar el ancho en su lugar
        if new_width > width:
            new_width = width
            new_height = int(width / aspect_ratio)

        # redimensionar la imagen y guardarla en la carpeta de salida
        resized_img = img.resize((new_width, new_height))
        output_filepath = os.path.join(output_folder, filename)
        resized_img.save(output_filepath)
