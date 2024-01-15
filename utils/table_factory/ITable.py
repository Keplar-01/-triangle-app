from abc import ABC, abstractmethod


class ITable(ABC):
    @abstractmethod
    def render(self, data):
        pass

    @abstractmethod
    def insert_row(self,  data, row):
        pass