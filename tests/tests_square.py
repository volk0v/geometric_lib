import unittest
import square

class SquareTestCase(unittest.TestCase):
    def test_area_CorrectSide(self):
        result = square.area(5)
        self.assertEqual(result, 25)

    def test_area_SideIsZero(self):
        with self.assertRaises(ValueError):
            square.area(0)

    def test_area_SideIsNegative(self):
        with self.assertRaises(ValueError):
            square.area(-1)

    def test_perimeter_CorrectSide(self):
        result = square.perimeter(5)
        self.assertEqual(result, 20)

    def test_perimeter_SideIsZero(self):
        with self.assertRaises(ValueError):
            square.perimeter(0)

    def test_perimeter_SideIsNegative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1)
