"""Database module the Memorization Tool application."""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Flashcard

engine = create_engine("sqlite:///flashcard.db?check_same_thread=False")

Base.metadata.create_all(engine)


def get_session() -> Session:
    """Create and return a new database session."""

    return Session(engine)


def add_flashcard_to_db(question: str, answer: str) -> None:
    """Add a new flashcard to the database."""

    with get_session() as session:
        flashcard = Flashcard(question=question, answer=answer)
        session.add(flashcard)
        session.commit()


def get_flashcards_from_db() -> list[type[Flashcard]]:
    """Retrieve all flashcards from the database."""

    with get_session() as session:
        flashcards = session.query(Flashcard).all()
        return flashcards


def update_flashcard_in_db(flashcard_id: int, new_question: str, new_answer: str) -> None:
    """Update an existing flashcard in the database."""

    with get_session() as session:
        flashcard = session.query(Flashcard).get(flashcard_id)
        if flashcard:
            flashcard.question = new_question
            flashcard.answer = new_answer
            session.commit()
