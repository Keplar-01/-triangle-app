from abc import ABC, abstractmethod


class ITable(ABC):
    @abstractmethod
    def render(self, data):
        pass






