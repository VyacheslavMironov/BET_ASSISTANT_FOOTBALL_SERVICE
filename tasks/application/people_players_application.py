from tasks.domain.entities.people_players import PeoplePlayers
from tasks.domain.services.people_players_service import PeoplePlayersService


class PeoplePlayersApplication(object):
    entity: PeoplePlayers

    def SetCollection(self, service:PeoplePlayersService=PeoplePlayersService()):
        for item in service.query_all()['data']:
            # 1 это футбол
            if item['sport_id'] == 1 and 'main_team' in item.keys():
                people_name = item['name'].split()
                service.add(
                    PeoplePlayers(
                        SportId=item['sport_id'],
                        TeamId=item['main_team']['id'],
                        LastName=people_name[0],
                        FirstName=people_name[1],
                        Image=item['photo'],
                        Slug=people_name[0] + '_' + people_name[1]
                    )
                )
