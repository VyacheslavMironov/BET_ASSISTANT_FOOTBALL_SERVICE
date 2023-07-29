from tasks.domain.entities.country_leagues import CountryLeagues
from tasks.domain.services.country_leagues_service import CountryLeaguesService
from tasks.domain.services.translate_service import TranslateService


class CountryLeaguesApplication(object):
    entity: CountryLeagues

    def SetCollection(self, service:CountryLeaguesService=CountryLeaguesService(), translate_service:TranslateService=TranslateService()):
        for item in service.query_all()['data']:
            # 1 это футбол
            if item['sport_id'] == 1 and item['section_id']:
                langs = translate_service.translate(item['name_translations']['en'])
                service.add(
                    CountryLeagues(
                        SportId=item['sport_id'],
                        SectionId=item['section_id'],
                        NameRu=langs['ru'].replace("'", " "),
                        NameEn=langs['en'].replace("'", " "),
                        NameDe=langs['de'].replace("'", " "),
                        NameFr=langs['fr'].replace("'", " "),
                        Image=item['logo'],
                        Slug=langs['en'].replace("'", " ").replace(' ', '_')
                    )
                )
