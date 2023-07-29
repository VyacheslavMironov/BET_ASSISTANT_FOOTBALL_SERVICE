from tasks.domain.abstract_repository.abstract_people_players_repository import AbstractPeoplePlayersRepository
from tasks.domain.entities.people_players import PeoplePlayers
from tasks.infrastructure.database.db_context import engine, Session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, ProgrammingError


class PeoplePlayersRepository(AbstractPeoplePlayersRepository):
    def add(self, context: PeoplePlayers) -> PeoplePlayers:
        with Session(autoflush=False, bind=engine) as session:
            try:
                session.execute(
                    text(f"""
                        INSERT INTO people_players(
                            \"SportId\", 
                            \"TeamId\", 
                            \"LastName\", 
                            \"FirstName\", 
                            \"Image\", 
                            \"Slug\"
                        )
                        VALUES(
                            {context.SportId}, 
                            {context.TeamId}, 
                            '{context.LastName}', 
                            '{context.FirstName}', 
                            '{context.Image}', 
                            '{context.Slug}'
                        );
                    """)
                )
                session.commit()
                session.close()
            except IntegrityError as e:
                pass
            except ProgrammingError as e:
                pass
        return context
