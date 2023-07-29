from abc import ABC, abstractmethod
from tasks.domain.entities.country_leagues import CountryLeagues


class AbstractCountryLeaguesRepository(ABC):
    @abstractmethod
    def add(self, context: CountryLeagues) -> CountryLeagues:
        pass
