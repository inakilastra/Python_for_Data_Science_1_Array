# DOCUMENTAR
def slice_me(family: list[list], start: int, end: int) -> list[list]:
    """ Truncates a 2D array given start and end indices.

    Args:
        family: A 2D array represented as a list of lists.
        start: Starting (inclusive) index for the slice.
        end: Ending (exclusive) index for the slice.

    Returns:
        A new array that is a slice of the original array.
    """

    if not isinstance(family, list) \
            or not all(isinstance(row, list) for row in family):
        raise TypeError("The 'family' argument must be a list of lists.")

    rows = len(family)
    cols = len(family[0]) if family else 0
    print(f"My shape is: ({rows}, {cols})")
    new_family = family[start:end]
    print(f"My new shape is: ({len(new_family)}, {cols})")
    return new_family


'''
tester.py
from array2D import slice_me

family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

'''

'''
def slice_me(family: list[list], start: int, end: int) -> list[list]:
    """ Trunca una matriz 2D dada unos índices de inicio y fin.

    Args:
        family: Una matriz 2D representada como una lista de listas.
        start: Índice de la primera fila a incluir (inclusivo).
        end: Índice de la primera fila a excluir (exclusivo).

    Returns:
        list[list]: Devuelve una nueva lista de listas (una nueva matriz).
    """

    # Verificar que 'family' una lista, y que cada elemento dentro de family
    # también sea una lista. Si no cumple con estas condiciones,
    # se lanza un error TypeError
    if not isinstance(family, list) \
            or not all(isinstance(row, list) for row in family):
        raise TypeError("El argumento 'family' debe ser una lista de listas.")

    # Obtener la forma de la matriz
    # Calculo el número de filas (rows) y columnas (cols) de la
    # matriz original. Imprimo la forma de la matriz original
    rows = len(family)
    cols = len(family[0]) if family else 0
    print(f"My shape is: ({rows}, {cols})")

    # MEJORA
    # Validar los índices los valores de start y end estén dentro de los
    # límites válidos de la matriz. Si están fuera de rango,
    # se lanzaría un ValueError.
    """
    if start < 0 or start >= rows or end < start or end > rows:
        raise ValueError("Los índices están fuera de rango.")
    """

    # Con el método de segmentación (slicing)extraigo las filas desde el índice
    # start (inclusivo) hasta el índice end (exclusivo) de la matriz original.
    # El resultado se almacena en new_family.
    new_family = family[start:end]
    print(f"My new shape is: ({len(new_family)}, {cols})")
    return new_family
'''
