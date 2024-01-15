from abc import ABC, abstractmethod


class IFigureTableStrategy(ABC):
    @abstractmethod
    def prepare_data(self, data):
        pass

    @abstractmethod
    def fill_table(self, data):
        pass

    @abstractmethod
    def insert_row(self, data, row_index):
        pass

    @abstractmethod
    def update_row(self, data, row_index):
        pass