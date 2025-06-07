import unittest
from src.ordenamientoQuicksort import ordenamiento_quick

class TestOrdenamientoQuicksort(unittest.TestCase):
    def test_ordenamiento_quicksort(self):
        lista = [("Julio", 6.0), ("Ana", 9.0), ("Luis", 7.5), ("Ariel", 5.5), ("Juan", 8.5), ("Macarena", 10.0), ("Santiago", 8.5)]
        resultado = ordenamiento_quick(lista)
        self.assertEqual(resultado, [("Santiago", 8.5), ("Macarena", 10.0), ("Luis", 7.5), ("Julio", 6.0), ("Juan", 8.5), ("Ariel", 5.5), ("Ana", 9.0)])