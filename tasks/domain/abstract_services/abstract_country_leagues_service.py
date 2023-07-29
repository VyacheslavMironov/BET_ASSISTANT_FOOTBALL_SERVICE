from abc import ABC, abstractmethod
from tasks.domain.entities.country_leagues import CountryLeagues


class AbstractCountryLeaguesService(ABC):
    @abstractmethod
    def query_all(self) -> dict or list:
        pass

    @abstractmethod
    def add(self, context: CountryLeagues) -> CountryLeagues:
        pass
