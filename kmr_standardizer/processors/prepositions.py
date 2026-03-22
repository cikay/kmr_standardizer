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
            pattern=r"(?i)\b(der\s*(barê|heqê))\b(.*?)\bde\b",
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
            pattern=r"(?i)\b(ji)\b((?:(?!\b(?:bi|di)\b).)*?)\bre\b",
            replacement=r"\1\2ra",  # replace ji ... re with ji ... ra
            category=CategoryTypes.PREPOSITION,
            name="ji ... re->ji ... ra",
        ),
        Rule(
            pattern=r"(?i)\b(bi)\b((?:(?!\b(?:ji|di)\b).)*?)\bre\b",
            replacement=r"\1\2ra",  # replace bi ... re with bi ... ra
            category=CategoryTypes.PREPOSITION,
            name="bi ... re->bi ... ra",
        ),
        Rule(
            pattern=r"(?i)\b(di)\b((?:(?!\b(?:bi|ji)\b).)*?)\bre\b",
            replacement=r"\1\2ra",  # replace di ... re with di ... ra
            category=CategoryTypes.PREPOSITION,
            name="di ... re->di ... ra",
        ),
        Rule(
            pattern=r"(?i)\b(jê|pê)([ \t]+)re\b",
            replacement=r"\1\2ra",  # preserve existing whitespace: "jê   re" -> "jê   ra"
            category=CategoryTypes.PREPOSITION,
            name="jê/pê/tê ... re->jê/pê/tê ... ra",
        ),
    ]
