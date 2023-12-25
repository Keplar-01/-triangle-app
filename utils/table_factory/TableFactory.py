from utils.table_factory.HtmlTable import HtmlTable
from utils.table_factory.QtTable import QtTable


class TableFactory:
    @staticmethod
    def create_table(table_type, *args):
        if table_type == "qt":
            return QtTable(*args)
        elif table_type == "html":
            return HtmlTable(*args)
        else:
            raise ValueError("Unknown table type")