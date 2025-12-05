import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_area_CorrectSideAndHeight(self):
        result = triangle.area(5, 10)
        self.assertEqual(result, 25)

    def test_area_SideIsZero(self):
        with self.assertRaises(ValueError):
            triangle.area(0, 10)

    def test_area_HeightIsZero(self):
        with self.assertRaises(ValueError):
            triangle.area(5, 0)

    def test_area_SideAndHeightAreZero(self):
        with self.assertRaises(ValueError):
            triangle.area(0, 0)

    def test_area_SideIsNegative(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, 10)

    def test_area_HeightIsNegative(self):
        with self.assertRaises(ValueError):
            triangle.area(5, -1)

    def test_area_SideAndHeightAreNegatives(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, -1)
