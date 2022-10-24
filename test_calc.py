import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 1)
        self.assertEqual(calc.add(-1, 2), -1)