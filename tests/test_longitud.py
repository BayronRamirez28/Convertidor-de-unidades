import unittest
from conversiones.longitud import (
    metros_a_kilometros, kilometros_a_metros,
    metros_a_millas, millas_a_metros,
    metros_a_pies, pies_a_metros
)

class TestLongitud(unittest.TestCase):
    def test_metros_a_kilometros(self):
        self.assertAlmostEqual(metros_a_kilometros(1000), 1)
        self.assertAlmostEqual(metros_a_kilometros(1500), 1.5)
    
    def test_kilometros_a_metros(self):
        self.assertEqual(kilometros_a_metros(1), 1000)
        self.assertEqual(kilometros_a_metros(1.5), 1500)
    
    def test_metros_a_millas(self):
        self.assertAlmostEqual(metros_a_millas(1609.34), 1)
        self.assertAlmostEqual(metros_a_millas(3218.68), 2)
    
    def test_millas_a_metros(self):
        self.assertAlmostEqual(millas_a_metros(1), 1609.34)
        self.assertAlmostEqual(millas_a_metros(2), 3218.68)
    
    def test_metros_a_pies(self):
        self.assertAlmostEqual(metros_a_pies(1), 3.28084)
        self.assertAlmostEqual(metros_a_pies(10), 32.8084)
    
    def test_pies_a_metros(self):
        self.assertAlmostEqual(pies_a_metros(3.28084), 1)
        self.assertAlmostEqual(pies_a_metros(32.8084), 10)

if __name__ == '__main__':
    unittest.main()