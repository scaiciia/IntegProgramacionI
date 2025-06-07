def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio][0] == objetivo:
            return lista[medio]
        elif lista[medio][0] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return None