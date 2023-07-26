from tasks.domain.abstract_services.abstract_section_service import AbstractSectionService
from tasks.domain.entities.section import Section
# from tasks.infrastructure.database.sport_repository import SportRepository
# from tasks.infrastructure.rapid.query_sport import SportQuery


class SportService(AbstractSportService):
    # __Repository: SportRepository
    # __Rapid: SportQuery

    def __init__(self) -> None:
        self.__Repository = SportRepository()
        self.__Rapid = SportQuery()
        super().__init__()

    def query_all(self) -> dict or list:
        return self.__Rapid.get_date()

    def add(self, context: Sport) -> Sport:
        return self.__Repository.add(context=context)
