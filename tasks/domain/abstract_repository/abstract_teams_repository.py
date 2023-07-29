from abc import ABC, abstractmethod
from tasks.domain.entities.teams import Teams


class AbstractTeamsRepository(ABC):
    @abstractmethod
    def add(self, context: Teams) -> Teams:
        pass
