import unittest
from src.busquedaSecuencial import busqueda_secuencial

class TestBusquedaSecuencial(unittest.TestCase):
    def test_busqueda_secuencial(self):
        lista = [("Juan", 85), ("Ana", 90), ("Luis", 78)]
        objetivo = "Ana"
        resultado = busqueda_secuencial(lista, objetivo)
        self.assertEqual(resultado, ("Ana", 90))

    def test_busqueda_no_encontrada(self):
        lista = [("Juan", 85), ("Ana", 90), ("Luis", 78)]
        objetivo = "Pedro"
        resultado = busqueda_secuencial(lista, objetivo)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()