import unittest
from image.funciones import sentgen_function, desgeneraliza, demostracion


class TestFuncionesImagen(unittest.TestCase):
    
    
    def assertNotEmpty(self, obj):
        self.assertTrue(obj)
    
    def test_sentgen(self):
        self.assertNotEmpty(sentgen_function('Sentimiento', 'Simple CNN', '50', 'SGD'))
        
        print('Prueba de introduccion de parametro COMPARA_ALGORITMO a nulo: \n')
        #sentgen_function('', 'Simple CNN', '50', 'SGD')
        
        print('Prueba de introduccion de parametro CSV a nulo: \n')
        #sentgen_function('Sentimiento', '', '50', 'SGD')
        
        print('Prueba de introduccion de parametro TOKENIZE a nulo: \n')
        #sentgen_function('Sentimiento', 'Simple CNN', '', 'SGD')
        
        print('Prueba de introduccion de dos parametro a nulo: \n')
        #sentgen_function('Genero', '', '', 'SGD')
    
    def test_desgeneraliza(self):
        self.assertEqual(desgeneraliza('Enfadado'), 'Enfado')
        

if __name__ == "__main__":
    unittest.main()