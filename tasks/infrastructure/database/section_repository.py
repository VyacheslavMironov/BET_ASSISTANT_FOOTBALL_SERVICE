from tasks.domain.abstract_repository.abstract_section_repository import AbstractSectionRepository
from tasks.domain.entities.section import Section
from tasks.infrastructure.database.db_context import engine, Session
from tasks.infrastructure.journal.logging import set_log
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, ProgrammingError


class SectionRepository(AbstractSectionRepository):
    def add(self, context: Section) -> Section:
        with Session(autoflush=False, bind=engine) as session:
            try:
                session.execute(
                    text(f"""
                        INSERT INTO sections(\"SportId\", \"NameRu\", \"NameEn\", \"NameDe\", \"NameFr\")
                        VALUES({context.SportId}, '{context.NameRu}', '{context.NameEn}', '{context.NameDe}', '{context.NameFr}');
                    """)
                )
                session.commit()
                session.close()
            except IntegrityError as e:
                set_log(e._message)
            except ProgrammingError as e:
                set_log("Ошибка! 2!!!")
                # raise Exception(f"Запись \"{context.Name}\" уже существует в таблице \"bet_assistant_db.publc.sports\"")
        return context
