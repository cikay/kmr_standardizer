import re

from .base import Processor
from kmr_standardizer.models import Rule, CategoryTypes


class PrepositionProcessor(Processor):
    rules = [
        Rule(
            pattern=r"\bde\b",
            replacement="da",  # replace de with da
            category=CategoryTypes.PREPOSITION,
        ),
        Rule(
            pattern=r"\bre\b",
            replacement="ra",  # replace re with ra
            category=CategoryTypes.PREPOSITION,
        ),
    ]

    def process(self, text: str) -> str:
        for rule in self.rules:
            text = re.sub(rule.pattern, rule.replacement, text)
        return text
