import json
from abc import ABC, abstractmethod
from tasks.domain.entities.sport import Sport


class AbstractSportService(ABC):
    @abstractmethod
    def query_all(self) -> dict or list:
        pass

    @abstractmethod
    def add(self, context: Sport) -> Sport:
        pass
