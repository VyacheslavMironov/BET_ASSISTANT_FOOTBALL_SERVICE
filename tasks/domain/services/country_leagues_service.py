from tasks.domain.abstract_services.abstract_country_leagues_service import AbstractCountryLeaguesService
from tasks.domain.entities.country_leagues import CountryLeagues
from tasks.infrastructure.database.country_leagues_repository import CountryLeaguesRepository
from tasks.infrastructure.rapid.query_count_leagues import CountLeaguesQuery


class CountryLeaguesService(AbstractCountryLeaguesService):
    __Repository: CountryLeaguesRepository
    __Rapid: CountLeaguesQuery

    def __init__(self) -> None:
        self.__Repository = CountryLeaguesRepository()
        self.__Rapid = CountLeaguesQuery()
        super().__init__()

    def query_all(self) -> dict or list:
        return self.__Rapid.get_date()

    def add(self, context: CountryLeagues) -> CountryLeagues:
        return self.__Repository.add(context=context)
