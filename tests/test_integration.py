import pytest

from kmr_standardizer.processors.prepositions import PrepositionProcessor


@pytest.fixture
def integration_test_processor():
    return PrepositionProcessor()


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            "De ka em vê hevokê îcar “çi qas” û “lê belê“yê bi hev ve binivîsîn û pirsa xwe bikin, bê ka ji hêla mehneyê ve çi diguhere",
            "De ka em vê hevokê îcar “çi qas” û “lê belê“yê bi hev ve binivîsîn û pirsa xwe bikin, bê ka ji hêla mehneyê ve çi diguhere",
        ),
        (
            "De îcar bifikirin ev tiştên li ser zimanê kurdî hatine gotin, eger ji bo erebî, ji bo farisî yan jî ji bo tirkî bihatina gotin kî dizane niha ew di çi rewşê û em jî di çi halî de bûn.",
            "De îcar bifikirin ev tiştên li ser zimanê kurdî hatine gotin, eger ji bo erebî, ji bo farisî yan jî ji bo tirkî bihatina gotin kî dizane niha ew di çi rewşê û em jî di çi halî da bûn.",
        ),
        (
            "De wê gavê mîna niha înternet û medyaya civakî jî tune bû",
            "De wê gavê mîna niha înternet û medyaya civakî jî tune bû",
        ),
        (
            "ez behsa paşdaçeka “de/da“yê bikim, ji lew re ew “de” yan jî “da” kîjan bê tercîhkirin jî tesîr li awayê rastnivîsînê nake.",
            "ez behsa paşdaçeka “de/da“yê bikim, ji lew ra ew “de” yan jî “da” kîjan bê tercîhkirin jî tesîr li awayê rastnivîsînê nake."
        ),
    ],
)
def test_does_not_replace_not_covered_de(input, expected, integration_test_processor):
    assert integration_test_processor.process(input) == expected
