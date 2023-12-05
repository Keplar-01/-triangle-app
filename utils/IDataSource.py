from abc import ABC, abstractmethod


class IDataSource(ABC):
    @abstractmethod
    def get_list(self):
        pass

