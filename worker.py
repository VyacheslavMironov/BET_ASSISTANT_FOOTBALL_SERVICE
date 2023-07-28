import asyncio
from tasks.application.engine import background
from tasks.application.sport_application import SportApplication
from tasks.application.section_application import SectionApplication


sport = SportApplication()
section = SectionApplication()


@background.task
def sports():
    return sport.SetCollection()

@background.task
def sections():
    return section.SetCollection()


sports.delay()
sections.delay()


# Запускаем воркер
if __name__ == '__main__':
    background.start()