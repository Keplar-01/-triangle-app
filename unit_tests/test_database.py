from django.test import TestCase
from main.models import Triangle


class TriangleModelTests(TestCase):

    def test_triangle_creation(self):
        triangle = Triangle.objects.create(first_side=3, second_side=4)
        saved_triangle = Triangle.objects.get(pk=triangle.pk)
        self.assertEqual(saved_triangle.first_side, 3.0)
        self.assertEqual(saved_triangle.second_side, 4.0)

    def test_delete_triangle(self):
        triangle = Triangle.objects.create(first_side=3, second_side=4)
        triangle_id = triangle.id
        triangle.delete()
        with self.assertRaises(Triangle.DoesNotExist):
            deleted_triangle = Triangle.objects.get(pk=triangle_id)
