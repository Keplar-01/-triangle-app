from .models import Triangle


class TriangleBuilder:
    def __init__(self):
        self.triangle = Triangle()

    def set_first_side(self, first_side: float):
        self.triangle.first_side = first_side
        return self

    def set_second_side(self, second_side: float):
        self.triangle.second_side = second_side
        return self

    def get_triangle(self):
        return self.triangle
