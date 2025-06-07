def busqueda_secuencial(lista, objetivo):
    for alumno, nota in lista:
        if alumno == objetivo:
            return (alumno, nota)
    return None