# DOCUMENTAR
def slice_me(family: list[list], start: int, end: int) -> list[list]:
    """Trunca una matriz 2D dada unos índices de inicio y fin.

    Args:
        family: Una matriz 2D representada como una lista de listas.
        start: Índice inicial (inclusivo) para el corte.
        end: Índice final (exclusivo) para el corte.

    Returns:
        Una nueva matriz que es una porción de la matriz original.
    """

    # Verificar que 'family' sea una lista de listas
    if not isinstance(family, list) \
        or not all(isinstance(row, list) for row in family):
        raise TypeError("El argumento 'family' debe ser una lista de listas.")

    # Obtener la forma de la matriz
    rows = len(family)
    cols = len(family[0]) if family else 0
    print(f"My shape is: ({rows}, {cols})")

    # Validar los índices
    # if start < 0 or start >= rows or end < start or end > rows:
    #  raise ValueError("Los índices están fuera de rango.")

    # Realizar el corte y devolver la nueva matriz
    new_family = family[start:end]
    print(f"My new shape is: ({len(new_family)}, {cols})")
    return new_family
