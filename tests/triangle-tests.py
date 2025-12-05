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

    def test_perimeter_CorrectSides(self):
        result = triangle.perimeter(3, 4, 5)
        self.assertEqual(result, 12)

    def test_perimeter_FirstSideIsZero(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(0, 4, 5)

    def test_perimeter_SecondSideIsZero(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 0, 5)

    def test_perimeter_ThirdSideIsZero(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 4, 0)

    def test_perimeter_AllSidesAreZero(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(0, 0, 0)

    def test_perimeter_FirstSideIsNegative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, 4, 5)

    def test_perimeter_SecondSideIsNegative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, -1, 5)

    def test_perimeter_ThirdSideIsNegative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 4, -1)

    def test_perimeter_AllSidesAreNegative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, -1, -1)
