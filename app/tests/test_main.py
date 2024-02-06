import unittest
from src.main import calcular_fatorial, verificar_palindromo

class TestFuncoes(unittest.TestCase):
    def test_calcular_fatorial(self):
        # Teste para calcular o fatorial de 5
        self.assertEqual(calcular_fatorial(5), 120)
        # Teste para calcular o fatorial de 0
        self.assertEqual(calcular_fatorial(0), 1)
        # Teste para calcular o fatorial de 1
        self.assertEqual(calcular_fatorial(1), 1)
        # Teste para calcular o fatorial de 10
        self.assertEqual(calcular_fatorial(10), 3628800)

    def test_verificar_palindromo(self):
        # Teste para verificar que "radar" é um palíndromo
        self.assertTrue(verificar_palindromo("radar"))
        # Teste para verificar que "python" não é um palíndromo
        self.assertFalse(verificar_palindromo("python"))
        # Teste para verificar que "anna" é um palíndromo
        self.assertTrue(verificar_palindromo("anna"))
        # Teste para verificar que "level" é um palíndromo
        self.assertTrue(verificar_palindromo("level"))
