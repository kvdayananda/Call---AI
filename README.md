# FlashLearn Spaced Repetition Learning Engine v2

Adaptive spaced-repetition flashcard system implementing Leitner box progression and review scheduling.

## Target Complexity & Language
- **Language:** python
- **Complexity:** intermediate

## Problem Statement
Students and developers need an algorithmic memory consolidation tool to review key concepts at optimal decay intervals.

## Key Features
- 5-box Leitner progression algorithm
- Review interval computation based on mastery box
- Deck progress and retention metrics
- Quiz runner evaluating answer accuracy

## Technology Stack
- Python 3.12
- Dataclasses
- Pytest


## Installation & Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running Unit Tests
```bash
pytest -v
```

---
*Generated, verified in Docker sandbox, and published automatically by [GitAuto AI](https://github.com).*
