import json
from abc import ABC, abstractmethod
from tasks.domain.entities.section import Section


class AbstractSectionService(ABC):
    @abstractmethod
    def query_all(self) -> dict or list:
        pass

    @abstractmethod
    def add(self, context: Section) -> Section:
        pass
