import numpy as np


def is_numeric(value):
    """ Check if the given value is numeric (integer or float).
        Return True if the value is of type int or float, and False
        otherwise.

    Args:
        value: The value to check. It can be of any type.

    Returns:
        bool: True if the value is a number (int or float), otherwise False.
    """
    return isinstance(value, (int, float))


def give_bmi(height: list[float], weight: list[float]) -> list[float]:
    """ Calculates the body mass index (BMI) for each individual given their
        height and weight.

    Args:
        height: List of heights in meters.
        weight: List of weights in kilograms.

    Returns:
        List of BMI values.
    """

    if len(height) != len(weight):
        print("The height and weight lists must be the same length.")
        return []
    if not all(is_numeric(h) for h in height) \
       or not all(is_numeric(w) for w in weight):
        print("All elements in lists must be numbers.")
        return []
    if any(h <= 0 for h in height) or any(w <= 0 for w in weight):
        print("Height and weight must be positive values.")
        return []
    height, weight = np.array(height), np.array(weight)
    bmi = weight / (height ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    """Compares each BMI value to a given limit and returns a boolean value
       indicating whether the BMI exceeds the limit.

    Args:
        bmi: List of BMI values.
        limit: BMI limit.

    Returns:
    List of boolean values ​​indicating whether the BMI exceeds the limit.
    """

    return [value > limit for value in bmi]


'''
# NumPy es una biblioteca de Python fundamental para realizar cálculos
# numéricos, especialmente con grandes conjuntos de datos.
import numpy as np


def is_numeric(value):
    """ Verifico si el valor dado es numérico (entero o flotante).
        devuelvo True si el valor es de tipo int o float, y False
        en caso contrario.

    Args:
        value: El valor a verificar. Puede ser de cualquier tipo.

    Returns:
        bool: True si el valor es un número (int o float), si no False.
    """
    return isinstance(value, (int, float))


def give_bmi(height: list[float], weight: list[float]) -> list[float]:
    """ Calcula el índice de masa corporal (IMC)(BMI) segun altura y peso.

    Args:
        height: Lista de alturas.
        weight: Lista de pesos.

    Returns:
        Lista de valores de IMC - BMI.
    """

    # Verifico que las listas de altura y peso tengan el mismo número de
    # elementos. Si no es así, indica un error y devuelve una lista vacía.
    if len(height) != len(weight):
        print("Las listas altura y peso deben tener la misma longitud.")
        return []
    # Con is_numeric me aseguro de que todos los elementos de las listas
    # sean números. Si no es así, indica un error y devuelve una lista vacía.
    if not all(is_numeric(h) for h in height) \
        or not all(is_numeric(w) for w in weight):
        print("Todos los elementos de las listas deben ser números.")
        return []
    # Me aseguro de que todos los elementos de las listas sean positivos.
    # Si no es así, indica un error y devuelve una lista vacía.
    if any(h <= 0 for h in height) or any(w <= 0 for w in weight):
        print("La altura y el peso deben ser valores positivos.")
        return []
    #  Convierto las listas de Python a arreglos de NumPy
    height, weight = np.array(height), np.array(weight)
    # Aplico la fórmula estándar del IMC (peso / altura^2) a todos los
    # elementos de los arreglos de forma simultánea.
    bmi = weight / (height ** 2)
    # Convierto el resultado de nuevo a una lista de Python para devolverlo.
    return bmi.tolist()



def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    """ Compara cada valor de IMC con un límite dado y devuelve un valor
        booleano indicando si el IMC supera el límite.

    Args:
        bmi: Lista de valores de IMC.
        limit: Límite de IMC.

    Returns:
        Lista de valores booleanos indicando si el IMC supera el límite.
    """

    return [value > limit for value in bmi]
'''

'''
tester.py

from give_bmi import give_bmi, apply_limit

height = [2.71, 2.62, 2.50]
weight = [165.3, 38.4, 40]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
'''
