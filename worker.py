import asyncio
from tasks.application.engine import background
from tasks.application.sport_application import SportApplication


sport = SportApplication()

@background.task
def sports():
    return sport.SetCollection()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(sports())
sports.delay()


# Запускаем воркер
if __name__ == '__main__':
    background.start()