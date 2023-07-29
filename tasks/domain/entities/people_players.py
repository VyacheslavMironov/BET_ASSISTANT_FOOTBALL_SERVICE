from dataclasses import dataclass


@dataclass
class PeoplePlayers:
    SportId: int
    TeamId: int
    LastName: str
    FirstName: str
    Image: str
    Slug: str
    
    def __init__(self, SportId, TeamId, LastName, FirstName, Image, Slug):
        self.SportId = SportId
        self.TeamId = TeamId
        self.LastName = LastName
        self.FirstName = FirstName
        self.Image = Image
        self.Slug = Slug
