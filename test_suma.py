import unittest
from suma import sumar

class testSumar(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3,5),8)
        self.assertEqual(sumar(-1,3),2)
        self.assertEqual(sumar(-100,-300),-400)

if __name__ == '__main__':
    unittest.main()
