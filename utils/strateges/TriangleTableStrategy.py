from model.builder import TriangleBuilder
from model.models import Triangle
from utils.data_sources.IDataSource import IDataSource
from utils.strateges.IFigureTableStrategy import IFigureTableStrategy
from utils.table_factory.ITable import ITable


class TriangleTableStrategy(IFigureTableStrategy):
    def __init__(self, table: ITable, data_source: IDataSource):
        super().__init__()
        self.table = table
        self.data_source = data_source

    def prepare_data(self, columns_names: list[str]):
        data = self.data_source.get_list(Triangle)
        table_data = []
        table_data.append(columns_names)
        for triangle in data:
            row = [triangle.id, triangle.first_side, triangle.second_side, triangle.hypotenuse, triangle.perimeter, triangle.area]
            table_data.append(row)
        return table_data

    def fill_table(self, columns_names: list[str]) -> None:
        return self.table.render(self.prepare_data(columns_names))

    def insert_row(self, data: list, row_index: int) -> None:
        builder = TriangleBuilder()
        triangle = builder.set_first_side(data[0]).set_second_side(data[1]).get_triangle()
        self.data_source.insert_item(triangle)

        new_data = [triangle.id] + data
        self.table.insert_row(new_data, row_index)

    def update_row(self, data: list, row_index: int) -> None:
        triangle_id = data[0]
        col_index = data[1]
        triangle = self.data_source.get_item(triangle_id, Triangle)
        if triangle:
            if col_index == 1:
                triangle.first_side = data[2]
            elif col_index == 2:
                triangle.second_side = data[2]
        self.data_source.update_item(triangle, Triangle)

