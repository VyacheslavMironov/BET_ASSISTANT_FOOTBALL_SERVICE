from tasks.application.engine import background
from tasks.application.sport_application import SportApplication
from tasks.application.section_application import SectionApplication
from tasks.application.country_leagues_application import CountryLeaguesApplication
from tasks.application.teams_application import TeamsApplication
from tasks.application.people_players_application import PeoplePlayersApplication


sport = SportApplication()
section = SectionApplication()
country_league = CountryLeaguesApplication()
team = TeamsApplication()
people_player = PeoplePlayersApplication()


# @background.task
# def sports():
#     return sport.SetCollection()

# @background.task
# def sections():
#     return section.SetCollection()

# @background.task
# def country_leagues():
#     return country_league.SetCollection()

# @background.task
# def teams():
#     return team.SetCollection()

@background.task
def people_players():
    return people_player.SetCollection()


# sports.delay()
# sections.delay()
# country_leagues.delay()
# teams.delay()
people_players.delay()


# Запускаем воркер
if __name__ == '__main__':
    background.start()