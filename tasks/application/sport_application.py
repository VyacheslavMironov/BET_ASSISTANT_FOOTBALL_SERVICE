from tasks.domain.entities.sport import Sport
from tasks.domain.services.sport_service import SportService
from tasks.domain.services.translate_service import TranslateService


class SportApplication(object):
    entity: Sport

    def SetCollection(self, service:SportService=SportService(), translate_service:TranslateService=TranslateService()):
        for item in service.query_all()['data']:
            if item['name'] == 'Football':
                langs = translate_service.translate(item['name'])
                service.add(
                    Sport(
                        NameRu=langs['ru'],
                        NameEn=langs['en'],
                        NameDe=langs['de'],
                        NameFr=langs['fr']
                    )
                )
