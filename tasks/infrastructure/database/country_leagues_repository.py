from tasks.domain.abstract_repository.abstract_country_leagues_repository import AbstractCountryLeaguesRepository
from tasks.domain.entities.country_leagues import CountryLeagues
from tasks.infrastructure.database.db_context import engine, Session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, ProgrammingError


class CountryLeaguesRepository(AbstractCountryLeaguesRepository):
    def add(self, context: CountryLeagues) -> CountryLeagues:
        with Session(autoflush=False, bind=engine) as session:
            try:
                session.execute(
                    text(f"""
                        INSERT INTO country_leagues(
                            \"SportId\", 
                            \"SectionId\", 
                            \"NameRu\", 
                            \"NameEn\", 
                            \"NameDe\", 
                            \"NameFr\",
                            \"Image\",
                            \"Slug\"
                        )
                        VALUES(
                            {context.SportId}, 
                            {context.SectionId}, 
                            '{context.NameRu}', 
                            '{context.NameEn}', 
                            '{context.NameDe}', 
                            '{context.NameFr}',
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
