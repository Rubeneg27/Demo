import unittest
from operaciones import sumar
from operaciones import restar
from operaciones import mult
from operaciones import div

class testSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3,5),8)
        self.assertEqual(sumar(-1,3),2)
        self.assertEqual(sumar(-100,-300),-400)

class testResta(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(restar(6,3),3)
        self.assertEqual(restar(-6,3),-9)
        self.assertEqual(restar(6,-3),9)
        self.assertEqual(restar(-6,-3),-3)

class testMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(mult(5,3),15)
        self.assertEqual(mult(-2,3),-6)
        self.assertEqual(mult(2,-3),-6)
        self.assertEqual(mult(-2,-3),6)

class testDividir(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(div(6,3),2)
        self.assertEqual(div(-6,3),-2)
        self.assertEqual(div(6,-3),-2)
        self.assertEqual(div(-6,-3),2)
        self.assertEqual(div(6,3),2)
    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            div(6, 0)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

if __name__ == '__main__':
    unittest.main()
