import unittest
print ("Hello, test!")
from kalkulatorpol import KalkulatorPol  

class TestKalkulatorPol(unittest.TestCase):

    def setUp(self):
        self.kalk = KalkulatorPol()

    def test_pole_kola(self):
        self.assertAlmostEqual(self.kalk.pole_kola(2), 12.56636, places=5)

    def test_pole_kwadratu(self):
        self.assertEqual(self.kalk.pole_kwadratu(3), 9)

    def test_pole_prostokata(self):
        self.assertEqual(self.kalk.pole_prostokata(4, 5), 20)

    def test_pole_trojkata(self):
        self.assertEqual(self.kalk.pole_trojkata(6, 2), 6)

    def test_oblicz_koło(self):
        self.assertAlmostEqual(self.kalk.oblicz("koło", 1), 3.14159, places=5)

    def test_oblicz_blad(self):
        with self.assertRaises(ValueError):
            self.kalk.oblicz("pięciokąt", 1, 2)

if __name__ == '__main__':
    unittest.main()