# Funcion de ordenamiento por metodo burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j][0] > lista[j+1][0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
