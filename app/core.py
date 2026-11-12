"""FlashLearn Core Engine."""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Flashcard:
    id: str
    front: str
    back: str
    box: int = 1
    review_count: int = 0

    def validate(self) -> None:
        if not self.front or not self.front.strip():
            raise ValueError("Card front cannot be empty.")
        if not self.back or not self.back.strip():
            raise ValueError("Card back cannot be empty.")
        if not (1 <= self.box <= 5):
            raise ValueError(f"Box must be between 1 and 5, got {self.box}")


class Deck:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards: List[Flashcard] = []

    def add_card(self, card_id: str, front: str, back: str) -> Flashcard:
        card = Flashcard(card_id, front, back)
        card.validate()
        self.cards.append(card)
        return card

    def record_attempt(self, card_id: str, is_correct: bool) -> Flashcard:
        for card in self.cards:
            if card.id == card_id:
                card.review_count += 1
                if is_correct:
                    card.box = min(5, card.box + 1)
                else:
                    card.box = 1
                return card
        raise KeyError(f"Card '{card_id}' not found.")

    def mastery_rate(self) -> float:
        if not self.cards:
            return 0.0
        scores = [(c.box - 1) / 4.0 for c in self.cards]
        return round(sum(scores) / len(scores) * 100.0, 1)
