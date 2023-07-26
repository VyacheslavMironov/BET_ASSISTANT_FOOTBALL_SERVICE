from abc import ABC, abstractmethod
from tasks.domain.entities.sport import Sport


class AbstractSportRepository(ABC):
    @abstractmethod
    def add(self, context: Sport) -> Sport:
        pass
