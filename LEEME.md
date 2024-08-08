# Python for Data Science

<h1>1 - Array</h1>

<br />

> Otros Lenguajes
>
> - [English](https://github.com/inakilastra/Python_for_Data_Science_1_Array/blob/main/README.md)

<br />

> [!IMPORTANT]  
> Al final de cada fichero tienes una explicación del código.

<br />

>
> - :white_check_mark: [Subject](#subject)
>
>   - :white_check_mark: [Exercise 00 Give my BMI](#exercise-00-give-my-bmi)
>
>   - :white_check_mark: [Exercise 01 2D array](#exercise-01-2d-array)
>
>   - :white_check_mark: [Exercise 02 load my image](#exercise-02-load-my-image)
>
>   - :white_check_mark: [Exercise 03 zoom on me](#exercise-03-zoom-on-me)
>
>   - :white_check_mark: [Exercise 04 rotate me](#exercise-04-rotate-me)
>
>   - :white_check_mark: [Exercise 05 Pimp my image](#exercise-05-pimp-my-image)

<br /><br />

>
> - :white_check_mark: [Evaluation](#evaluation) 

<br /><br /><br /><br />

## <h2>Subject</h2>

<h3>Reglas generales</h3>

- Debes renderizar tus módulos desde una computadora en el cluster usando una máquina virtual:
    - Puedes elegir el sistema operativo que usarás para tu máquina virtual
    - Tu máquina virtual debe tener todo el software necesario para realizar tu proyecto. Este software debe estar configurado e instalado.
- O puedes usar la computadora directamente en caso de que las herramientas estén disponibles.
    - Asegúrate de tener el espacio en tu sesión para instalar lo que necesitas para todos los módulos (usa goinfre si tu campus lo tiene)
    - Debes tener todo instalado antes de las evaluaciones
- Tus funciones no deben cerrarse inesperadamente (error de segmentación, error de bus, doble liberación, etc.) además de comportamientos indefinidos. Si esto sucede, tu proyecto se considerará no funcional y recibirá un 0 durante la evaluación.
- Te alentamos a crear programas de prueba para tu proyecto, aunque este trabajo **no tendrá que ser entregado y no será calificado**. Te dará la oportunidad de probar fácilmente tu trabajo y el de tus compañeros. Encontrarás esas pruebas especialmente útiles durante tu defensa. De hecho, durante la defensa, eres libre de usar tus pruebas y/o las pruebas del compañero que estás evaluando.
- Envía tu trabajo al repositorio git que se te haya asignado. Solo se calificará el trabajo en el repositorio git. Si se le asigna a Deepthought la calificación de tu trabajo, se hará después de las evaluaciones de tus compañeros. Si ocurre un error en cualquier sección de tu trabajo durante la calificación de Deepthought, la evaluación se detendrá.
- Debes usar la versión Python 3.10
- Puedes usar cualquier función incorporada si no está prohibida en el ejercicio.
- Tus importaciones de biblioteca deben ser explícitas, por ejemplo, debes "importar numpy como np". Importar "desde pandas import *" no está permitido y obtendrás 0 en el ejercicio.
- No hay ninguna variable global.
- ¡Por Odin, por Thor! ¡Usa tu cerebro!

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **subir** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>A partir de ahora debes seguir estas reglas adicionales</h3>

- No hay código en el ámbito global. ¡Usa funciones!
- Cada programa debe tener su main y no ser un simple script:

```python
def main():
# your tests and your error handling
if __name__ == "__main__":
main()
```

- Cualquier excepción no capturada invalidará los ejercicios, incluso en el caso de un error que se te pidió que probaras.
- Todas tus funciones deben tener una documentación (__doc__)
- Tu código debe estar en la norma
- pip install flake8
- alias norminette=flake8

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

### <h3>Exercise 00 Give my BMI</h3>

Turn-in directory : ex00/<br />
Files to turn in : give_bmi.py<br />
Allowed functions : numpy or any lib of table manipulation<br />

Tu función, give_bmi, toma 2 listas de números enteros o flotantes en la entrada y devuelve una lista de valores de BMI.
Tu función, apply_limit, acepta una lista de números enteros o flotantes y un número entero que representa un límite como parámetros. Devuelve una lista de valores booleanos (Verdadero si está por encima del límite).
Debes manejar casos de error si las listas no tienen el mismo tamaño, no son int o float...

El prototipo de las funciones es:

```python
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
#your code here

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#your code here
```

Tú tester.py:

```python
from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
```

Resultado esperado:

```
$> python tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

### <h3>Exercise 01 2D array</h3>

Turn-in directory : ex01/<br />
Files to turn in : array2D.py<br />
Allowed functions : numpy or any lib of table manipulation<br />

Escribe una función que tome como parámetros una matriz 2D, imprima su forma y devuelva una versión truncada de la matriz en función de los argumentos iniciales y finales proporcionados.
Debes utilizar el método de segmentación.
Debes gestionar los casos de error si las listas no tienen el mismo tamaño, no son una lista...

El prototipo de la función es:

```python
def slice_me(family: list, start: int, end: int) -> list:
#your code here
```

Tú tester.py:

```python
from array2D import slice_me

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```

Resultado esperado:

```
$> python test_array2D.py
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

### <h3>Exercise 02 load my image</h3>

Turn-in directory : ex02/<br />
Files to turn in : load_image.py<br />
Allowed functions : all libs for load images and table manipulation<br />

Debes escribir una función que cargue una imagen, imprima su formato y su contenido de píxeles en formato RGB.
Debes manejar, al menos, el formato JPG y JPEG.
Debes manejar cualquier error con un mensaje de error claro.

Así es como debería ser el prototipo:

```python
def ft_load(path: str) -> array: (you can return to the desired format)
#your code here
```

Tú tester.py:

```python
from load_image import ft_load

print(ft_load("landscape.jpg"))
```

Resultado esperado:

```
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
$>
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

### <h3>Exercise 03 zoom on me</h3>

Turn-in directory : ex03/<br />
Files to turn in : load_image.py, zoom.py<br />
Allowed functions : all libs for load, manipulate, display image and table
manipulation<br />

Crea un programa que cargue la imagen "animal.jpeg", imprima información sobre ella y la muestre después de hacer zoom.

- El tamaño en píxeles en los ejes X e Y
- El número de canales
- El contenido en píxeles de la imagen.
- Mostrar la escala en los ejes X e Y de la imagen

Si algo sale mal, el programa no debe detenerse de repente y debe manejar cualquier error con un mensaje claro.

Resultado esperado:

```
$> python zoom.py
The shape of image is: (768, 1024, 3)
[[[120 111 132]
[139 130 151]
[155 146 167]
...
[120 156 94]
[119 154 90]
[118 153 89]]]
New shape after slicing: (400, 400, 1) or (400, 400)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
$>
```

Resultado esperado:

<p align="center">
  <img src="https://github.com/inakilastra/Python_for_Data_Science_1_Array/blob/main/img/animal1.png?raw=true" alt="Animal zoom."/>
</p>

```
La matriz después del corte y el área de zoom pueden ser diferentes.
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

### <h3>Exercise 04 rotate me</h3>

Turn-in directory : ex4/<br />
Files to turn in : load_image.py, rotate.py<br />
Allowed functions : all libs for load, manipulate, display image and table
manipulation<br />

Crea un programa que cargue la imagen "animal.jpeg", corte una parte cuadrada de ella y transpóngala para producir la imagen que se muestra a continuación. Debería mostrarla, imprimir la nueva forma y los datos de la imagen después de la transposición.

Resultado esperado:

```python
$> python rotate.py
The shape of image is: (400, 400, 1) or (400, 400)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
New shape after Transpose: (400, 400)
[[167 180 194 ... 64 50 72]
...
[115 116 119 ... 102 104 103]]
$>
```

```
Tu matriz después de la transposición puede ser diferente.
Puedes buscar el método de transposición, podría ayudarte...
```

```
Debes hacer la transposición tú mismo, no se permite ninguna biblioteca para la transposición
```

Resultado esperado:

<p align="center">
  <img src="https://github.com/inakilastra/Python_for_Data_Science_1_Array/blob/main/img/animal2.png?raw=true" alt="Animal zoom."/>
</p>

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

### <h3>Exercise 05 Pimp my image</h3>

Turn-in directory : ex05/<br />
Files to turn in : load_image.py, pimp_image.py<br />
Allowed functions : all libs for load, manipulate, display image and table
manipulation<br />

Debes desarrollar 5 funciones capaces de aplicar una variedad de filtros de color a las imágenes, manteniendo la forma de la imagen.

Así es como se deben crear los prototipos:

```python
def ft_invert(array) -> array:
#your code here

def ft_red(array) -> array:
#your code here

def ft_green(array) -> array:
#your code here

def ft_blue(array) -> array:
#your code here

def ft_grey(array) -> array:
#your code here
```

Tienes algunos operadores de restricción para cada función: (solo puedes usar los que se proporcionan, no tienes que usarlos todos)

- invert: =, +, -, *
- red: =, *
- green: =, -
- blue: =
- grey: =, /

Tú tester.py:

```python
from load_image import ft_load
from pimp_image import ft_invert
...

array = ft_load("landscape.jpg")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)
```

Resultado esperado: (las cadenas de documentos pueden ser diferentes)

```
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
...
Inverts the color of the image received.
$>
```

Resultado esperado: (debes mostrar las imágenes transformadas)

<p align="center">
  <img src="https://github.com/inakilastra/Python_for_Data_Science_1_Array/blob/main/img/landscapes.png?raw=true" alt="Landscape."/>
</p>

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

## <h2>Evaluation</h2>

<h3>Pautas</h3>

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **subir** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />