from tasks.domain.abstract_repository.abstract_sport_repository import AbstractSportRepository
from tasks.domain.entities.sport import Sport
from tasks.infrastructure.database.db_context import engine, Session
from tasks.infrastructure.journal.logging import set_log
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError


class SportRepository(AbstractSportRepository):
    def add(self, context: Sport) -> Sport:
        with Session(autoflush=False, bind=engine) as session:
            try:
                session.execute(
                    text(f"""
                        INSERT INTO sports(\"NameRu\", \"NameEn\", \"NameDe\", \"NameFr\")
                        VALUES('{context.NameRu}', '{context.NameEn}', '{context.NameDe}', '{context.NameFr}');
                    """)
                )
                session.commit()
                session.close()
            except IntegrityError as e:
                set_log(e._message)
                # raise Exception(f"Запись \"{context.Name}\" уже существует в таблице \"bet_assistant_db.publc.sports\"")
        return context
