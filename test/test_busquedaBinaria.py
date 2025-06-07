import unittest
from src.busquedaBinaria import busqueda_binaria

class TestBusquedaBinaria(unittest.TestCase):
    def test_busqueda_binaria(self):
        lista = [("Ana", 9.0), ("Ariel", 5.5), ("Juan", 8.5), ("Julio", 6.0), ("Luis", 7.5), ("Macarena", 10.0), ("Santiago", 8.5)]
        lista.sort()  # Aseguramos que la lista esté ordenada
        objetivo = "Juan"
        resultado = busqueda_binaria(lista, objetivo)
        self.assertEqual(resultado, ("Juan", 8.5))

    def test_busqueda_no_encontrada(self):
        lista = [("Ana", 9.0), ("Ariel", 5.5), ("Juan", 8.5), ("Julio", 6.0), ("Luis", 7.5), ("Macarena", 10.0), ("Santiago", 8.5)]
        lista.sort()  # Aseguramos que la lista esté ordenada
        objetivo = "Pedro"
        resultado = busqueda_binaria(lista, objetivo)
        self.assertIsNone(resultado)