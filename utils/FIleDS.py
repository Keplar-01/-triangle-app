from database import Session
from model.models import Triangle
from model.builder import TriangleBuilder
from utils.IDataSource import IDataSource


class FileDS(IDataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_list(self) -> list[Triangle] | list:
        session = Session()
        try:
            with open(self.file_path, 'r') as file:
                data = []
                for line in file:
                    content = line.strip()
                    first_side, second_side = map(float, content.split())
                    builder = TriangleBuilder()
                    triangle = builder.set_first_side(first_side).set_second_side(second_side).get_triangle()
                    data.append(triangle)
            return data
        except Exception as e:
            return []
