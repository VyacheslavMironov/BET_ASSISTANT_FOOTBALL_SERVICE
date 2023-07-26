from tasks.infrastructure.rapid.translate import TranslateRapidApi


class TranslateService:
    out: dict

    def __init__(self) -> None:
        self.out = dict()
    
    def serialize(self, param:dict) -> str or None:
        return param['data']['translatedText'] if param['status'].lower() == "success" else None

    def translate(self, data:str, langs=('ru', 'de', 'fr')) -> dict:
        self.out['en'] = data
        for lang in langs:
            repository = TranslateRapidApi(
                SourceLanguage='en', 
                TargetLanguage=lang, 
                Text=data
            )
            self.out[lang] = self.serialize(repository.text_translate_query())
        return self.out
