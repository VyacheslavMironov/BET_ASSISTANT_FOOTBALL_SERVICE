from tasks.domain.entities.teams import Teams
from tasks.domain.services.teams_service import TeamsService
from tasks.domain.services.translate_service import TranslateService


class TeamsApplication(object):
    entity: Teams

    def SetCollection(self, service:TeamsService=TeamsService()):
        for item in service.query_all()['data']:
            # 1 это футбол
            if item['sport_id'] == 1:
                service.add(
                    Teams(
                        SportId=item['sport_id'],
                        Name=item['name'].replace("'", " "),
                        Image=item['logo'],
                        Slug=item['name'].replace("'", " "),
                    )
                )
