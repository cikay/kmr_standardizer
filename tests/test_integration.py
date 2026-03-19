import pytest

from kmr_standardizer.processors.prepositions import PrepositionProcessor


@pytest.fixture
def integration_test_processor():
    return PrepositionProcessor()


def test_does_not_replace_not_covering_de_ka(integration_test_processor):
    text = "De ka em vê hevokê îcar “çi qas” û “lê belê“yê bi hev ve binivîsîn û pirsa xwe bikin, bê ka ji hêla mehneyê ve çi diguhere"
    assert integration_test_processor.process(text) == text
