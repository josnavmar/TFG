import unittest
from text.funciones import comparacion_algoritmos , tokenize


class TestFuncionesImagen(unittest.TestCase):
    
    
    def assertNotEmpty(self, obj):
        self.assertTrue(obj)
    
    def test_comparacion_algoritmos(self):
        self.assertNotEmpty(comparacion_algoritmos())
    
    def test_tokenize_equal(self):
        self.assertEqual(tokenize('Enfado'),['enfad'])
        
    def test_tokenize_empty(self):
        self.assertNotEmpty(tokenize('Enfado'))


if __name__ == "__main__":
    unittest.main()

