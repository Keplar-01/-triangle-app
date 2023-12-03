import math


class Triangle:
    def __init__(self, first_side, second_side):
        self.__first_side = first_side
        self.__second_side = second_side

    def get_first_side(self):
        return self.__first_side

    def get_second_side(self):
        return self.__second_side

    @property
    def hypotenuse(self):
        if self.is_right:
            return (self.__first_side ** 2 + self.__second_side ** 2) ** 0.5
        else:
            return None

    @property
    def is_right(self):
        return math.isclose(min(self.__first_side, self.__second_side) / max(self.__first_side, self.__second_side), 1)

    @property
    def area(self):
        if self.is_right:
            return self.__first_side * self.__second_side / 2
        else:
            return None

    @property
    def perimeter(self):
        return self.__first_side + self.__second_side + self.hypotenuse

    def __str__(self):
        return f'A={self.__first_side} B={self.__second_side} C={self.hypotenuse}'
