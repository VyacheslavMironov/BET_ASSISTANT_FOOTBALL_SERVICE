from tasks.domain.abstract_services.abstract_teams_service import AbstractTeamsService
from tasks.domain.entities.teams import Teams
from tasks.infrastructure.database.teams_repository import TeamsRepository
from tasks.infrastructure.rapid.query_teams import TeamsQuery


class TeamsService(AbstractTeamsService):
    __Repository: TeamsRepository
    __Rapid: TeamsQuery

    def __init__(self) -> None:
        self.__Repository = TeamsRepository()
        self.__Rapid = TeamsQuery()
        super().__init__()

    def query_all(self) -> dict or list:
        return self.__Rapid.get_date()

    def add(self, context: Teams) -> Teams:
        return self.__Repository.add(context=context)
