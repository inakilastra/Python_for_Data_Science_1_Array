import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and return it as a NumPy array.

    Parameters:
    path (str): The path to the image file to be loaded.

    Returns:
    np.ndarray: A NumPy array representing the loaded image.

    Raises:
    AssertionError: If the image format is wrong or the file is not found.

    Loads an image from the given path and performs checks to ensure
    compatibility and validity. Only JPG and JPEG formats are supported. If the
    file does not exist or the format is not supported, an Error is raised.
    The image is then converted to a NumPy array and its shape is printed.

    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        print(
            f"The shape of Image is: {img.size[1]},{img.size[0]}, {img.layers}"
            )
        return np.array(img)
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return ""


'''
tester.py
from load_image import ft_load

print("ft_load(\"landscape.jpg\")")
print(ft_load("landscape.jpg"))
print("ft_load(\"landscape.png\")")
print(ft_load("landscape.png"))
print("ft_load(\"landzcape.jpg\")")
print(ft_load("landzcape.jpg"))
# Imprimir la forma de la imagen print(f"The shape of Image is:
# (", {img_array.size[1]}, {img.size[0]}, {img.layers}")")
'''

'''
def ft_load(path: str) -> np.ndarray:
    """Carga una imagen y devuelve un array NumPy con los valores RGB.

    Args:
        path: Ruta al archivo de imagen.

    Returns:
        Un array de 3 dimensiones representando la imagen en formato RGB.
    """

    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        # Cargar la imagen usando PIL
        img = Image.open(path)

        # Convertir la imagen a un array NumPy
        img_array = np.array(img)

        # Imprimir la forma de la imagen
        print("The shape of image is:", img_array.shape)

        return img_array
    except FileNotFoundError:
        print("Error: No se encontró el archivo de imagen.")
    except IOError:
        print("Error: No se pudo cargar la imagen. Verifique el formato.")
'''
