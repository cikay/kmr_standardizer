import pytest

from kmr_standardizer.processors.prepositions import PrepositionProcessor
from kmr_standardizer.processors.oblique import ObliqueProcessor


@pytest.fixture
def processor():
    return PrepositionProcessor()


@pytest.fixture
def oblique_processor():
    return ObliqueProcessor()
