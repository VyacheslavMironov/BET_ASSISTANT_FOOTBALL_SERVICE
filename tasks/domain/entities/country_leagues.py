from dataclasses import dataclass


@dataclass
class CountryLeagues:
    SportId: int
    SectionId: int
    NameRu: str
    NameEn: str
    NameDe: str
    NameFr: str
    Image: str
    Slug: str
    
    def __init__(self, SportId, SectionId, NameRu, NameEn, NameDe, NameFr, Image, Slug):
        self.SportId = SportId
        self.SectionId = SectionId
        self.NameRu = NameRu
        self.NameEn = NameEn
        self.NameDe = NameDe
        self.NameFr = NameFr
        self.Image = Image
        self.Slug = Slug
