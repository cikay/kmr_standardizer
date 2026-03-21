import re

from .base import Processor
from kmr_standardizer.models import Rule, CategoryTypes


class PrepositionProcessor(Processor):
    rules = [
        Rule(
            pattern=r"(?i)(\bdi\b)([^;!?\n]+?)\bde\b",
            replacement=r"\1\2da",  # replace di ... de with di ... da
            category=CategoryTypes.PREPOSITION,
            name="di...de->di...da",
        ),
        # replace der barê/derbarê/der heqê/derheqê ... de with der barê/derbarê/der heqê/derheqê ... da
        Rule(
            pattern=r"(?i)(\bder\s*(barê|heqê))(.*?)\bde\b",
            replacement=r"\1\3da",
            category=CategoryTypes.PREPOSITION,
            name="derbarê/derheqê ... de ->derbarê/derheqê ... da",
        ),
        Rule(
            pattern=r"(?i)\btê\s+de\b",
            replacement=r"tê da",  # replace tê de with tê da
            category=CategoryTypes.PREPOSITION,
            name="tê de->tê da",
        ),
        Rule(
            pattern=r"\bre\b",
            replacement="ra",  # replace re with ra
            category=CategoryTypes.PREPOSITION,
            name="bi...re->bi...ra",
        ),
    ]
