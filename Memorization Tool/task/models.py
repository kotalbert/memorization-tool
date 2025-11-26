"""Models for the Memorization Tool app."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Flashcard(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)

    def __repr__(self):
        return f"Flashcard(id={self.id!r}, question={self.question!r}, answer={self.answer!r})"
