from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def zoom_image(image_array, zoom_factor=0.5):
    try:
        # Calculate the new dimensions
        original_shape = image_array.shape
        new_x = int(original_shape[1] * zoom_factor)
        new_y = int(original_shape[0] * zoom_factor)
        
        # Perform the zoom by slicing the array
        zoomed_image = image_array[:new_y, :new_x]
        
        # Print new image shape and data
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)
        
        return zoomed_image
    except Exception as e:
        print(f"An error occurred while zooming the image: {e}")
        return None

def display_image(image_array):
    try:
        plt.imshow(image_array)
        plt.axis('on')  # Show axes
        plt.show()
    except Exception as e:
        print(f"An error occurred while displaying the image: {e}")

if __name__ == "__main__":
    image_path = "animal.jpeg"
    img_array, shape = ft_load(image_path)
    
    if img_array is not None:
        zoomed_image = ft_load(img_array)
        if zoomed_image is not None:
            display_image(zoomed_image)

'''
$> python zoom.py
The shape of image is: (768, 1024, 3)
[[[120 111 132]
[139 130 151]
[155 146 167]
...
[120 156 94]
[119 154 90]
[118 153 89]]]
New shape after slicing: (400, 400, 1) 
or (400, 400)

New shape after slicing: (384, 512, 1)


[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
$>
'''

'''
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np

def zoom_on_image(image: np.ndarray, zoom_factor: float) -> np.ndarray:
    """
    Realiza un zoom en el centro de la imagen.

    Args:
        image (np.ndarray): La imagen original.
        zoom_factor (float): El factor de zoom.

    Returns:
        np.ndarray: La imagen después del zoom.
    """
    # Obtener las dimensiones de la imagen
    height, width, _ = image.shape

    # Calcular las nuevas dimensiones
    new_height = int(height / zoom_factor)
    new_width = int(width / zoom_factor)

    # Calcular los bordes para el recorte
    top = (height - new_height) // 2
    left = (width - new_width) // 2
    bottom = top + new_height
    right = left + new_width

    # Recortar la imagen
    zoomed_image = image[top:bottom, left:right]

    return zoomed_image

def main():
    # Cargar la imagen
    image = ft_load("animal.jpeg")

    if image is not None:
        # Realizar el zoom en la imagen
        zoom_factor = 2  # Cambia esto para ajustar el nivel de zoom
        zoomed_image = zoom_on_image(image, zoom_factor)

        # Imprimir la nueva forma de la imagen
        print("\033[0;92mNew shape after slicing: ",zoomed_image.shape,
            "\033[0;39m")
        print("\033[0;92m",zoomed_image,"\033[0;39m")
        # Mostrar la imagen original y la imagen con zoom
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].imshow(image)
        axes[0].set_title("Original Image")
        axes[1].imshow(zoomed_image)
        axes[1].set_title("Zoomed Image")
        plt.show()
    else:
        print("Failed to load image.")

if __name__ == "__main__":
    main()
'''

'''
from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os


def print_rows_firstelem(arr, int):
    """
    Print a formatted display of the first elements
    in each row of a given array.

    Parameters:
    arr (array-like): The input array containing elements to be displayed.
    int (int): An integer specifying the display format: 0 for single brackets,
               1 for triple brackets.

    Iterates through the rows of the input array and displays the first
    elements of each row in a formatted manner. The display format is
    determined by the 'int' parameter. For 'int' equal to 0, single
    brackets are used to enclose the elements, while for 'int' equal
    to 1, triple brackets are used.
    """
    count = 0
    for row in arr:
        count += 1
    length = count
    count = 0
    for row in arr:
        if count == 0:
            if int == 1:
                print("[[[", row[0], "]", sep="")
            else:
                print("[[", row[0], sep="")
        if count > 0 and count < 3 or count > length - 4:
            if int == 1:
                if count == length - 1:
                    print("  [", row[0], "]]]", sep="")
                elif count < length - 1:
                    print("  [", row[0], "]", sep="")
            else:
                if count == length - 1:
                    print("  ", row[0], "]]", sep="")
                else:
                    print("  ", row[0], sep="")
        if count == 2:
            print("  ...")
        count += 1


def main():
    """
    Load, process, and display an image based on command-line arguments.

    This function serves as the main entry point of the script. It loads an
    image from the command-line argument, performs various image processing
    operations, and displays the resulting images. The script supports
    cropping, grayscale conversion, and zoomed image display. Errors related
    to file format and existence are caught and displayed.
    """
    try:
        path = sys.argv[1]
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        image = Image.open(path)
        if image is None:
            raise AssertionError("Failed to load image.")

        print_rows_firstelem(ft_load(path), 0)
        image.show()

        zoomed_image = image.crop((400, 100, 800, 600))
        zoomed_image.save("zoomed_image.jpg")
        print(f"New shape after cropping: {zoomed_image.size}")

        grayscale_image = zoomed_image.convert("L")
        grayscale_image.show()
        print_rows_firstelem(np.array(grayscale_image), 1)

        plt.imshow(zoomed_image)
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()


'''
