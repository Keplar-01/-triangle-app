from utils.IDataSource import IDataSource
from utils.Triangle import RightTriangle


class FileDS(IDataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_list(self) -> list[RightTriangle] | list:
        try:
            with open(self.file_path, 'r') as file:
                data = []
                for line in file:
                    content = line.strip()
                    first_side, second_side = map(float, content.split())
                    data.append(RightTriangle(first_side, second_side))
            return data
        except Exception as e:
            return []
