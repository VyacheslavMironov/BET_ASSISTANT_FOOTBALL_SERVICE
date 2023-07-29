from abc import ABC, abstractmethod
from tasks.domain.entities.people_players import PeoplePlayers


class AbstractPeoplePlayersService(ABC):
    @abstractmethod
    def query_all(self) -> dict or list:
        pass

    @abstractmethod
    def add(self, context: PeoplePlayers) -> PeoplePlayers:
        pass
