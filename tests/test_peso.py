import unittest
from conversiones.peso import kilogramos_a_libras, libras_a_kilogramos

class TestPeso(unittest.TestCase):
    def test_kilogramos_a_libras(self):
        self.assertAlmostEqual(kilogramos_a_libras(1), 2.20462)
        self.assertAlmostEqual(kilogramos_a_libras(2), 4.40924)
    
    def test_libras_a_kilogramos(self):
        self.assertAlmostEqual(libras_a_kilogramos(2.20462), 1)
        self.assertAlmostEqual(libras_a_kilogramos(4.40924), 2)

if __name__ == '__main__':
    unittest.main()