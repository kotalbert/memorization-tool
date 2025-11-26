"""Database module the Memorization Tool application."""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base

engine = create_engine("sqlite:///flashcard.db?check_same_thread=False")

Base.metadata.create_all(engine)


def get_session() -> Session:
    """Create and return a new database session."""

    return Session(engine)
