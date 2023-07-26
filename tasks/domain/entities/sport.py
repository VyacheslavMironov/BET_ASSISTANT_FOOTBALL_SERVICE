from dataclasses import dataclass


@dataclass
class Sport:
    NameRu: str
    NameEn: str
    NameDe: str
    NameFr: str
    
    def __init__(self, NameRu, NameEn, NameDe, NameFr):
        self.NameRu = NameRu
        self.NameEn = NameEn
        self.NameDe = NameDe
        self.NameFr = NameFr