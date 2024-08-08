# Python for Data Science

<h1>1 - Array</h1>

<br />

> [!NOTE] 
> Other Languages
>
> - [Castellano](https://github.com/inakilastra/Python_for_Data_Science_1_Array/blob/main/LEEME.md)

<br />

> [!IMPORTANT]  
> At the end of each file you have an explanation of the code.

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

<h3>General rules</h3>

- You have to render your modules from a computer in the cluster either using a virtual machine:
    - You can choose the operating system to use for your virtual machine
    - Your virtual machine must have all the necessary software to realize your project. This software must be configured and installed.
- Or you can use the computer directly in case the tools are available.
    - Make sure you have the space on your session to install what you need for all the modules (use the goinfre if your campus has it)
    - You must have everything installed before the evaluations
- Your functions should not quit unexpectedly (segmentation fault, bus error, double free, etc) apart from undefined behaviors. If this happens, your project will be considered non functional and will receive a 0 during the evaluation.
- We encourage you to create test programs for your project even though this work **won’t have to be submitted and won’t be graded**. It will give you a chance to easily test your work and your peers’ work. You will find those tests especially useful during your defence. Indeed, during defence, you are free to use your tests and/or the tests of the peer you are evaluating.
- Submit your work to your assigned git repository. Only the work in the git repository will be graded. If Deepthought is assigned to grade your work, it will be done after your  peer-evaluations. If an error happens in any section of your work during Deepthought’s grading, the evaluation will stop.
- You must use the Python 3.10 version
- You can use any built-in function if it is not prohibited in the exercise.
- Your lib imports must be explicit, for example you must "import numpy as np". Importing "from pandas import *" is not allowed, and you will get 0 on the exercise.
- There is no global variable.
- By Odin, by Thor! Use your brain!!!

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

<h3>Specific instructions of the day</h3>

- No code in the global scope. Use functions!
- Each program must have its main and not be a simple script:

```python
def main():
# your tests and your error handling
if __name__ == "__main__":
main()
```

- Any exception not caught will invalidate the exercices, even in the event of an error that you were asked to test.
- You can use any built-in function if it is not prohibited in the exercise.
- All your functions must have a documentation (__doc__)
- Your code must be at the norm
    - pip install flake8
    - alias norminette=flake8

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br />

### <h3>Exercise 00 Give my BMI</h3>

Turn-in directory : ex00/<br />
Files to turn in : give_bmi.py<br />
Allowed functions : numpy or any lib of table manipulation<br />

Your function, give_bmi, take 2 lists of integers or floats in input and returns a list of BMI values.
Your function, apply_limit, accepts a list of  integers or floats and an integer representing a limit as parameters. It returns a list of booleans (True if above the limit).
You have to handle error cases if the lists are not the same size, are not int or float...

The prototype of functions is:

```python
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
#your code here

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#your code here
```

Your tester.py:

```python
from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
```

Expected output:

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

Write a function that takes as parameters a 2D array, prints its shape, and returns a truncated version of the array based on the provided start and end arguments.
You must use the slicing method.
You have to handle error cases if the lists are not the same size, are not a list ...

The prototype of function is:

```python
def slice_me(family: list, start: int, end: int) -> list:
#your code here
```

Your tester.py:

```python
from array2D import slice_me

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```

Expected output:

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

You need to write a function that loads an image, prints its format, and its pixels content in RGB format.
You have to handle, at least, JPG and JPEG format.
You need to handle any error with a clear error message

Here’s how it should be prototyped :

```python
def ft_load(path: str) -> array: (you can return to the desired format)
#your code here
```

Your tester.py:

```python
from load_image import ft_load

print(ft_load("landscape.jpg"))
```

Expected output:

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

Create a program that should load the image "animal.jpeg", print some information about it and display it after "zooming".

- The size in pixel on both X and Y axis
- The number of channel
- The pixel content of the image.
- Display the scale on the x and y axis on the image

If anything went wrong, the program must not stop abruptly and handle any error with a clear message.

Expected output:

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

Expected output:

<p align="center">
  <img src="https://github.com/inakilastra/Python_for_Data_Science_1_Array/blob/main/img/animal1.png?raw=true" alt="Animal zoom."/>
</p>

```
Your array after slicing and the zoom area may be different.
```

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

### <h3>Exercise 04 rotate me</h3>

Turn-in directory : ex4/<br />
Files to turn in : load_image.py, rotate.py<br />
Allowed functions : all libs for load, manipulate, display image and table
manipulation<br />

Make a program which must load the image "animal.jpeg", cut a square part from it and transpose it to produce the image below. It should display it, print the new shape and the data of the image after the transpose.

Expected output:

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
Your array after the transpose can be different.
You can look for the transpose method, it could help you ...
```

```
You have to do the transpose yourself, no library is allowed for the transpose
```

Expected output:

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

You need to develop 5 functions capable of applying a variety of color filters to images, while keeping the image shape the same.

Here’s how they should be prototyped :

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

You have some restriction operators for each function: (you can only use those given, you don’t have to use them all)

- invert: =, +, -, *
- red: =, *
- green: =, -
- blue: =
- grey: =, /

Your tester.py:

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

Expected output: (docstrings can be different)

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

Expected output: (you must display the images transformed)

<p align="center">
  <img src="https://github.com/inakilastra/Python_for_Data_Science_1_Array/blob/main/img/landscapes.png?raw=true" alt="Landscape."/>
</p>

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />

## <h2>Evaluation</h2>

<h3>Guidelines</h3>

<br /><br />
[:arrow_up::arrow_up::arrow_up::arrow_up::arrow_up: **top** :arrow_up::arrow_up::arrow_up::arrow_up::arrow_up:](#python-for-data-science)
<br /><br /><br /><br />