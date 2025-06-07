# Funcion que realiza una búsqueda secuencial en una lista de tuplas
def busqueda_secuencial(lista, objetivo):
    for alumno, nota in lista:
        if alumno == objetivo:
            return (alumno, nota)
    return None