import unittest
from database import Session
from model.models import Base, Triangle

class TestTriangleModel(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close_all()

    def test_triangle_creation(self):
        triangle = Triangle(first_side=3, second_side=4)
        self.session.add(triangle)
        self.session.commit()

        saved_triangle = self.session.query(Triangle).filter_by(id=triangle.id).first()
        self.assertEqual(saved_triangle.first_side, 3.0)
        self.assertEqual(saved_triangle.second_side, 4.0)

    def test_delete_triangle(self):
        triangle = Triangle(first_side=3, second_side=4)
        self.session.add(triangle)
        self.session.commit()

        triangle_id = triangle.id
        self.session.delete(triangle)
        self.session.commit()

        with self.assertRaises(Exception):  # SQLAlchemy не бросает специфического исключения для отсутствия записи
            deleted_triangle = self.session.query(Triangle).filter_by(id=triangle_id).one()

if __name__ == '__main__':
    unittest.main()