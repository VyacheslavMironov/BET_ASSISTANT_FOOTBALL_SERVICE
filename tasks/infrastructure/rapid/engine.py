from dataclasses import dataclass
from dotenv import dotenv_values


config  = {
    **dotenv_values('.env')
}

@dataclass
class EngineRapidApi():
    Url: str
    Querystring: dict
    Headers: dict

    def __init__(self):
        self.Url = config["API_URL"]
        self.Querystring = {"page":"1"}
        self.Headers = {
            "X-RapidAPI-Key": f'{config["API_KEY"]}', 
            "X-RapidAPI-Host": f'{config["API_HOST"]}'
        }
