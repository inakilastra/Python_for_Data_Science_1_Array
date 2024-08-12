import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Carga una imagen desde el archivo especificado y devuelve su contenido de
    píxeles en formato RGB.

    Args:
        path (str): La ruta del archivo de imagen.

    Returns:
        np.ndarray: Un array numpy que contiene los valores de los píxeles en
        formato RGB.
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
        """ print("\033[0;92mThe shape of image is: ",image_array.shape,
            "\033[0;39m")
            print("\033[0;92m",image_array,"\033[0;39m")
        """
        return image_array
    except Exception as error:
        print(f"\033[38;5;209mError: {error}\033[0;39m")
        return ""
    

'''
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
