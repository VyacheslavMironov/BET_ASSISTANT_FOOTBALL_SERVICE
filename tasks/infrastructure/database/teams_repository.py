from tasks.domain.abstract_repository.abstract_teams_repository import AbstractTeamsRepository
from tasks.domain.entities.teams import Teams
from tasks.infrastructure.database.db_context import engine, Session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, ProgrammingError


class TeamsRepository(AbstractTeamsRepository):
    def add(self, context: Teams) -> Teams:
        with Session(autoflush=False, bind=engine) as session:
            try:
                session.execute(
                    text(f"""
                        INSERT INTO teams(
                            \"SportId\", 
                            \"Name\", 
                            \"Image\", 
                            \"Slug\"
                        )
                        VALUES(
                            {context.SportId}, 
                            '{context.Name}', 
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
