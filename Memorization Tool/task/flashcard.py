"""Flashcard class for a memorization tool."""


class Flashcard:
    """A class representing a flashcard with a question and an answer."""

    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer
