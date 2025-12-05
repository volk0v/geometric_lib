import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_area_CorrectSides(self):
        result = rectangle.area(5, 10)
        self.assertEqual(result, 50)

    def test_area_CorrectSidesButReversed(self):
        result = rectangle.area(10, 5)
        self.assertEqual(result, 50)

    def test_area_FirstSideIsZero(self):
        with self.assertRaises(ValueError):
            rectangle.area(0, 5)

    def test_area_SecondSideIsZero(self):
        with self.assertRaises(ValueError):
            rectangle.area(5, 0)

    def test_area_BothSidesAreZero(self):
        with self.assertRaises(ValueError):
            rectangle.area(0, 0)

    def test_area_FirstSideIsNegative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)   

    def test_area_SecondSideIsNegative(self):
        with self.assertRaises(ValueError):
            rectangle.area(5, -1)        

    def test_area_BothSidesAreNegative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, -1)   
