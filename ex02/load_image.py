import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """ Loads an image from the specified file and returns its pixel content
        in RGB format.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: A numpy array containing pixel values ​​in RGB format.
    """

    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            print("\033[38;5;209mOnly JPG and JPEG formats are supported."
                  "\033[0;39m")
            return ""
        if not os.path.exists(path):
            print("\033[38;5;209mFile not found:", path, "\033[0;39m")
            return ""
        image = Image.open(path)
        image = image.convert('RGB')
        image_array = np.array(image)
        print("\033[0;92mThe shape of image is: ", image_array.shape,
              "\033[0;39m")
        return image_array
    except Exception as error:
        print(f"\033[38;5;209mError: {error}\033[0;39m")
        return ""


'''
tester.py
from load_image import ft_load

print("> ft_load(\"landscape.jpg\")")
print(ft_load("landscape.jpg"))
print("\n> ft_load(\"landscape.png\")")
print(ft_load("landscape.png"))
print("\n> ft_load(\"landzcape.jpg\")")
print(ft_load("landzcape.jpg"))

'''

'''
# Se importa para verificar la existencia del archivo en la ruta especificada.
import os
# Se utiliza para convertir la imagen a un array NumPy y realizar operaciones
# numéricas en los píxeles.
import numpy as np
# Se importa para trabajar con la carga y manipulación de la imagen.
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """ Carga una imagen desde el archivo especificado y devuelve su contenido
        de píxeles en formato RGB.

    Args:
        path (str): La ruta del archivo de imagen.

    Returns:
        np.ndarray: Un array numpy que contiene los valores de los píxeles en
        formato RGB.
    """
    # El bloque try intenta ejecutar el código dentro de él.
    # Si ocurre algún error, se ejecuta el código dentro del bloque except.
    try:
        # Se convierte la ruta del archivo a minúsculas (path.lower()) y se
        # verifica si termina con ".jpg" o ".jpeg" usando endswith.
        if not path.lower().endswith(("jpg", "jpeg")):
            print("\033[38;5;209mOnly JPG and JPEG formats are supported."
                  "\033[0;39m")
            return ""
        # Se utiliza os.path.exists(path) para verificar si el archivo existe
        # en la ruta especificada.
        if not os.path.exists(path):
            print(f"\033[38;5;209mFile not found:", path, "\033[0;39m")
            return ""
        # Cargar la imagen con Image.open(path) de PIL para cargar la imagen
        # desde la ruta especificada.
        image = Image.open(path)
        # Convertir la imagen a RGB usando el método convert('RGB') de PIL.
        image = image.convert('RGB')
        # Convertir usando el método convert('RGB') de PIL.
        image_array = np.array(image)
        # Imprimir la forma de la imagen con utiliza image_array.shape para
        # Obtener las dimensiones de la imagen (alto, ancho, canales de color)
        print("\033[0;92mThe shape of image is: ", image_array.shape,
              "\033[0;39m")
        return image_array
    except Exception as error:
        print(f"\033[38;5;209mError: {error}\033[0;39m")
        return ""
'''
