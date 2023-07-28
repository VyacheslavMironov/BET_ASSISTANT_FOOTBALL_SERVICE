from tasks.domain.abstract_services.abstract_section_service import AbstractSectionService
from tasks.domain.entities.section import Section
from tasks.infrastructure.database.section_repository import SectionRepository
from tasks.infrastructure.rapid.query_section import SectionQuery


class SectionService(AbstractSectionService):
    __Repository: SectionRepository
    __Rapid: SectionQuery

    def __init__(self) -> None:
        self.__Repository = SectionRepository()
        self.__Rapid = SectionQuery()
        super().__init__()

    def query_all(self) -> dict or list:
        return self.__Rapid.get_date()

    def add(self, context: Section) -> Section:
        return self.__Repository.add(context=context)
