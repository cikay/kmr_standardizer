import pytest

from kmr_standardizer.processors.prepositions import PrepositionProcessor


@pytest.fixture
def processor():
    return PrepositionProcessor()
