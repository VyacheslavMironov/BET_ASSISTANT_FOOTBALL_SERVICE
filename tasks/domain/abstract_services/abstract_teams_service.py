from abc import ABC, abstractmethod
from tasks.domain.entities.teams import Teams


class AbstractTeamsService(ABC):
    @abstractmethod
    def query_all(self) -> dict or list:
        pass

    @abstractmethod
    def add(self, context: Teams) -> Teams:
        pass
