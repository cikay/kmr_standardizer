from dataclasses import dataclass
from typing import Union, Callable

from enum import Enum


@dataclass
class Rule:
    pattern: str
    replacement: Union[str, Callable]
    category: str
    name: str


class CategoryTypes(str, Enum):
    PREPOSITION = "PREPOSITION"
    OBLIQUE = "OBLIQUE"
