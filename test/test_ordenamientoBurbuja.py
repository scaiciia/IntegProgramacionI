import unittest
from src.ordenamientoBurbuja import ordenamiento_burbuja

class TestOrdenamientoBurbuja(unittest.TestCase):
    def test_ordenamiento_burbuja(self):
        lista = [("Julio", 6.0), ("Ana", 9.0), ("Luis", 7.5), ("Ariel", 5.5), ("Juan", 8.5), ("Macarena", 10.0), ("Santiago", 8.5)]
        resultado = ordenamiento_burbuja(lista)
        self.assertEqual(resultado, [("Ana", 9.0), ("Ariel", 5.5), ("Juan", 8.5), ("Julio", 6.0), ("Luis", 7.5), ("Macarena", 10.0), ("Santiago", 8.5)])