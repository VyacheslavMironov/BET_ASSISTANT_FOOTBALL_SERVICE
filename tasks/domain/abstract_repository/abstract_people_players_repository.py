from abc import ABC, abstractmethod
from tasks.domain.entities.people_players import PeoplePlayers


class AbstractPeoplePlayersRepository(ABC):
    @abstractmethod
    def add(self, context: PeoplePlayers) -> PeoplePlayers:
        pass
