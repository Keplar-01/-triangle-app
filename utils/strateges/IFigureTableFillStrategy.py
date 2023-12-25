from abc import ABC, abstractmethod


class IFigureTableFillStrategy(ABC):
    @abstractmethod
    def prepare_data(self, data):
        pass

    @abstractmethod
    def fill_table(self, data):
        pass