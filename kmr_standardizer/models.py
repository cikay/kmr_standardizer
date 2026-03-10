from dataclasses import dataclass

from enum import Enum


@dataclass
class Example:
    input: str
    output: str


@dataclass
class Rule:
    pattern: str
    replacement: str
    category: str
    examples: list[Example]


class CategoryTypes(str, Enum):
    PREPOSITION = "PREPOSITION"
