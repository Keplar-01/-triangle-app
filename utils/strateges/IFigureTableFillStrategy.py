from abc import ABC, abstractmethod


class IFigureTableFillStrategy(ABC):
    @abstractmethod
    def set_up_columns(self, columns):
        pass

    @abstractmethod
    def set_up_rows(self, data):
        pass

    @abstractmethod
    def fill_table(self):
        pass