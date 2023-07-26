from dotenv import dotenv_values
from requests import post


config  = {
    **dotenv_values('.env')
}

class TranslateRapidApi():
    Url: str
    Headers: dict
    Payload: dict
    SourceLanguage: str
    TargetLanguage: str
    Text: str

    def __init__(self, SourceLanguage, TargetLanguage, Text):
        self.Url = config["API_URL_TRANSLATE"]
        self.Headers = {
            "X-RapidAPI-Key": f'{config["API_KEY_TRANSLATE"]}', 
            "X-RapidAPI-Host": f'{config["API_HOST_TRANSLATE"]}'
        }
        self.Payload = {
            "source_language": SourceLanguage,
            "target_language": TargetLanguage,
            "text": Text
        }

    def text_translate_query(self):
        query = post(
            url=self.Url,
            data=self.Payload,
            headers=self.Headers
        )
        return query.json()
