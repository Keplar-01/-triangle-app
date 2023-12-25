import unittest
from database import Session
from model.models import Triangle
from model.builder import TriangleBuilder


class TestTriangleModel(unittest.TestCase):
    builder = TriangleBuilder()
    triangle = builder.set_first_side(3).set_second_side(4).get_triangle()

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close_all()

    def test_triangle_creation(self):
        builder = TriangleBuilder()
        triangle = builder.set_first_side(3).set_second_side(4).get_triangle()
        self.session.add(triangle)
        self.session.commit()

        saved_triangle = self.session.query(Triangle).filter_by(id=triangle.id).first()
        self.assertEqual(saved_triangle.first_side, 3.0)
        self.assertEqual(saved_triangle.second_side, 4.0)

    def test_delete_triangle(self):
        builder = TriangleBuilder()
        triangle = builder.set_first_side(3).set_second_side(4).get_triangle()
        self.session.add(triangle)
        self.session.commit()

        triangle_id = triangle.id
        self.session.delete(triangle)
        self.session.commit()

        with self.assertRaises(Exception):  # SQLAlchemy не бросает специфического исключения для отсутствия записи
            deleted_triangle = self.session.query(Triangle).filter_by(id=triangle_id).one()


if __name__ == '__main__':
    unittest.main()
