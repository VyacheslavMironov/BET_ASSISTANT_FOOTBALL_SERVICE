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
                pass
            except ProgrammingError as e:
                pass
        return context
