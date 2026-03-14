from dataclasses import dataclass

from enum import Enum


@dataclass
class Rule:
    pattern: str
    replacement: str
    category: str
    name: str


class CategoryTypes(str, Enum):
    PREPOSITION = "PREPOSITION"
