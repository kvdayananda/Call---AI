"""FlashLearn Main Application."""
from app.core import Deck


class LearningSession:
    def __init__(self, deck_name: str = "Default") -> None:
        self.deck = Deck(deck_name)

    def enroll_card(self, cid: str, front: str, back: str) -> dict:
        c = self.deck.add_card(cid, front, back)
        return {"card_id": c.id, "box": c.box, "status": "enrolled"}

    def practice_card(self, cid: str, is_correct: bool) -> dict:
        c = self.deck.record_attempt(cid, is_correct)
        return {
            "card_id": c.id,
            "new_box": c.box,
            "deck_mastery": self.deck.mastery_rate(),
        }
