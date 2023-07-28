from tasks.domain.entities.section import Section
from tasks.domain.services.section_service import SectionService
from tasks.domain.services.translate_service import TranslateService


class SectionApplication(object):
    entity: Section

    def SetCollection(self, service:SectionService=SectionService(), translate_service:TranslateService=TranslateService()):
        for item in service.query_all()['data']:
            # 1 это футбол
            if item['sport_id'] == 1:
                langs = translate_service.translate(item['name'])
                service.add(
                    Section(
                        SportId=item['sport_id'],
                        NameRu=langs['ru'].replace("'", " "),
                        NameEn=langs['en'].replace("'", " "),
                        NameDe=langs['de'].replace("'", " "),
                        NameFr=langs['fr'].replace("'", " "),
                    )
                )
