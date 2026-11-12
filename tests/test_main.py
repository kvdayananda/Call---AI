"""Tests for FlashLearn."""
import pytest
from app.core import Deck, Flashcard
from app.main import LearningSession


def test_card_validation():
    c = Flashcard("c1", "What is Big-O?", "Asymptotic time complexity", box=1)
    c.validate()

    with pytest.raises(ValueError):
        Flashcard("c2", "", "answer").validate()


def test_leitner_progression():
    deck = Deck("Algorithms")
    deck.add_card("1", "Q1", "A1")

    c = deck.record_attempt("1", True)
    assert c.box == 2
    c = deck.record_attempt("1", True)
    assert c.box == 3

    c = deck.record_attempt("1", False)
    assert c.box == 1


def test_mastery_calculation():
    session = LearningSession("Python")
    session.enroll_card("1", "Q1", "A1")
    session.enroll_card("2", "Q2", "A2")

    session.practice_card("1", True)
    res = session.practice_card("2", True)
    assert res["deck_mastery"] == 25.0
