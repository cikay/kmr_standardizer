import re
from abc import ABC

from kmr_standardizer.models import Rule


class Processor(ABC):
    rules: list[Rule] = []

    def process(self, text: str) -> str:
        for rule in self.rules:
            text = re.sub(rule.pattern, rule.replacement, text)
        return text
