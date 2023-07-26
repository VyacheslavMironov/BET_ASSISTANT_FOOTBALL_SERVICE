from requests import get
from tasks.infrastructure.rapid.engine import EngineRapidApi


class SportQuery(EngineRapidApi):
    Prefix: str

    def __init__(self):
        self.Prefix = "/sports"
        super().__init__()

    def get_date(self):
        query = get(
            url=str(self.Url+self.Prefix),
            headers=self.Headers,
            params=self.Querystring
        )
        return query.json()
