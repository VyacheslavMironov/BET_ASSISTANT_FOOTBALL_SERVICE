from dotenv import dotenv_values
from requests import get


config  = {
    **dotenv_values('.env')
}

class TranslateRapidApi():
    Url: str
    Headers: dict
    Querystring : dict

    def __init__(self, SourceLanguage, TargetLanguage, Text):
        self.Url = config["API_URL_TRANSLATE"]
        self.Headers = {
            "X-RapidAPI-Key": f'{config["API_KEY_TRANSLATE"]}', 
            "X-RapidAPI-Host": f'{config["API_HOST_TRANSLATE"]}'
        }
        self.Querystring = {
            "langpair": f'{SourceLanguage}|{TargetLanguage}',
            "q": Text,
            "mt":"1",
            "onlyprivate":"0",
            "de":"a@b.c"
        }

    def text_translate_query(self):
        query = get(
            url=self.Url,
            params=self.Querystring,
            headers=self.Headers
        )
        return query.json()
