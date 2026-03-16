import re

from .base import Processor
from kmr_standardizer.models import Rule, CategoryTypes


class PrepositionProcessor(Processor):
    rules = [
        Rule(
            pattern=r"(?i)(\bdi\b)([^.;:!?\n]+?)\bde\b",
            replacement=r"\1\2da",  # replace di ... de with di ... da
            category=CategoryTypes.PREPOSITION,
            name="di...de->di...da",
        ),
        Rule(
            pattern=r"(?i)\btê\s+de\b",
            replacement=r"tê da",  # replace tê de with tê da
            category=CategoryTypes.PREPOSITION,
            name="tê de->tê da",
        ),
        Rule(
            pattern=r"(?i)(\bji\b)((?:(?!\b(?:bi|di|der heqê|derheqê|der barê|derbarê|tê|pê|jê)\b)[^.!?\n])*?)\bde\b",
            replacement=r"\1\2da",  # replace ji ... de with ji ... da
            category=CategoryTypes.PREPOSITION,
            name="ji...de->ji...da",
        ),
        Rule(
            pattern=r"\bre\b",
            replacement="ra",  # replace re with ra
            category=CategoryTypes.PREPOSITION,
            name="bi...re->bi...ra",
        ),
    ]

    def process(self, text: str) -> str:
        for rule in self.rules:
            text = re.sub(rule.pattern, rule.replacement, text)
        return text
