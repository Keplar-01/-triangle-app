from database import Session
from model.models import Triangle
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
                    data.append(Triangle(first_side, second_side))
            return data
        except Exception as e:
            return []
