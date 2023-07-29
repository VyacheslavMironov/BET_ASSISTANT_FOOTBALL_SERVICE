from tasks.domain.abstract_services.abstract_people_players_service import AbstractPeoplePlayersService
from tasks.domain.entities.people_players import PeoplePlayers
from tasks.infrastructure.database.people_players_repository import PeoplePlayersRepository
from tasks.infrastructure.rapid.query_people_players import PeoplePlayersQuery


class PeoplePlayersService(AbstractPeoplePlayersService):
    __Repository: PeoplePlayersRepository
    __Rapid: PeoplePlayersQuery

    def __init__(self) -> None:
        self.__Repository = PeoplePlayersRepository()
        self.__Rapid = PeoplePlayersQuery()
        super().__init__()

    def query_all(self) -> dict or list:
        return self.__Rapid.get_date()

    def add(self, context: PeoplePlayers) -> PeoplePlayers:
        return self.__Repository.add(context=context)
