def ordenamiento_quick(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x[0] > pivote[0]]

    """Se modifica ya que la original no maneja los elementos iguales al pivote 
    (es decir, si hay tuplas con el mismo valor en [0] que el pivote, se perderán)."""
    iguales = [x for x in lista if x[0] == pivote[0]]

    derecha = [x for x in lista if x[0] < pivote[0]]
    return ordenamiento_quick(izquierda) + iguales + ordenamiento_quick(derecha)
