from dataclasses import dataclass


@dataclass
class Teams:
    SportId: int
    Name: str
    Image: str
    Slug: str
    
    def __init__(self, SportId, Name, Image, Slug):
        self.SportId = SportId
        self.Name = Name
        self.Image = Image
        self.Slug = Slug
