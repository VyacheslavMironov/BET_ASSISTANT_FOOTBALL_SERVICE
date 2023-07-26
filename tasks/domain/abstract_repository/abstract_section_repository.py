from abc import ABC, abstractmethod
from tasks.domain.entities.section import Section


class AbstractSectionRepository(ABC):
    @abstractmethod
    def add(self, context: Section) -> Section:
        pass
