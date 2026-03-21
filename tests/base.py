import pytest

from kmr_standardizer.processors.prepositions import PrepositionProcessor



class BaseTest:
    rule_name: str

    def setup_method(self):
        self._original_rules = PrepositionProcessor.rules
        PrepositionProcessor.rules = [
            r for r in self._original_rules if r.name == self.rule_name
        ]

    def teardown_method(self):
        PrepositionProcessor.rules = self._original_rules
