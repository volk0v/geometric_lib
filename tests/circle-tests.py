import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_area_CorrectRadius(self):
        result = circle.area(10)
        self.assertAlmostEqual(result, 314.159, 3)

    def test_area_NegativeRadius(self):
        with self.assertRaises(ValueError):
            circle.area(-10)
    
    def test_perimeter_CorrectRadius(self):
        result = circle.perimeter(10)
        self.assertAlmostEqual(result, 62.832, 3)

    def test_perimeter_NegativeRadius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-10)
