import unittest
from model.builder import TriangleBuilder


class TestTriangle(unittest.TestCase):

    def setUp(self):
        builder1 = TriangleBuilder()
        builder2 = TriangleBuilder()
        self.triangle1 = builder1.set_first_side(3).set_second_side(4).get_triangle()
        self.triangle2 = builder2.set_first_side(5).set_second_side(12).get_triangle()

    def test_hypotenuse(self):
        self.assertEqual(self.triangle1.hypotenuse, 5)
        self.assertEqual(self.triangle2.hypotenuse, 13)

    def test_area(self):
        self.assertEqual(self.triangle1.area, 6)
        self.assertEqual(self.triangle2.area, 30)

    def test_perimeter(self):
        self.assertEqual(self.triangle1.perimeter, 12)
        self.assertEqual(self.triangle2.perimeter, 30)

    def test_str(self):
        self.assertEqual(str(self.triangle1), 'A=3 B=4 C=5.0')
        self.assertEqual(str(self.triangle2), 'A=5 B=12 C=13.0')

if __name__ == '__main__':
    unittest.main()
