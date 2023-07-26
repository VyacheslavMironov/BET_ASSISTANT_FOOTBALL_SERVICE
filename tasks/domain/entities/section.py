from dataclasses import dataclass


@dataclass
class Section:
    SportId: int
    NameRu: str
    NameEn: str
    NameDe: str
    NameFr: str
    
    def __init__(self, SportId, NameRu, NameEn, NameDe, NameFr):
        self.SportId = SportId
        self.NameRu = NameRu
        self.NameEn = NameEn
        self.NameDe = NameDe
        self.NameFr = NameFr