from django.test import TestCase
from main.models import Triangle


class TestTriangle(TestCase):

    def setUp(self):
        self.triangle1 = Triangle(first_side=3, second_side=4)
        self.triangle2 = Triangle(first_side=5, second_side=12)

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
