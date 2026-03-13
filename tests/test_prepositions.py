import pytest

from kmr_standardizer.processors.prepositions import PrepositionProcessor


@pytest.fixture
def processor():
    return PrepositionProcessor()


class TestDeToDA:
    """Tests for di ... de → di ... da preposition rule."""

    def test_no_match(self, processor):
        assert processor.process("ez diçim malê") == "ez diçim malê"

    def test_simple_replacement(self, processor):
        assert processor.process("di mal de") == "di mal da"

    def test_empty_string(self, processor):
        assert processor.process("") == ""

    def test_multiple_occurrences(self, processor):
        text = "di mal de û di bajêr de"
        expected = "di mal da û di bajêr da"
        assert processor.process(text) == expected

    @pytest.mark.parametrize(
        "input,output",
        [
            (
                "di destê min de çi heye?",
                "di destê min de çi heye?",
            ),
            ("dengê xalê min", "dengê xalê min"),
        ],
    )
    def test_does_not_replace_inside_words(self, input, output, processor):
        """'de' inside words like should not be replaced."""
        assert processor.process(input) == output

    def test_replacement_before_punctuation(self, processor):
        assert processor.process("di nav malbatan de,") == "di nav malbatan da,"

    @pytest.mark.parametrize(
        "input,output",
        [
            (
                "Di dema pandemîyê de, mirov li malê man û li kokên xwe gerîyan.",
                "Di dema pandemîyê da, mirov li malê man û li kokên xwe gerîyan.",
            ),
            (
                "Di envanterên Tirkiyeyê de 300-400 destxetên Kurdî hene ku hîn ne dîjîtal in",
                "Di envanterên Tirkiyeyê da 300-400 destxetên Kurdî hene ku hîn ne dîjîtal in",
            ),
        ],
    )
    def test_case_insensitive(self, input, output, processor):
        assert processor.process(input) == output

    @pytest.mark.parametrize(
        "input,output",
        [
            (
                "Berî çend salan, muzîka kurdî bi piranî di nav malbatan de, di dawetan de an jî di radyoyan de dihat guhdarîkirin.",
                "Berî çend salan, muzîka kurdî bi piranî di nav malbatan da, di dawetan da an jî di radyoyan da dihat guhdarîkirin.",
            ),
        ],
    )
    def test_preserves_surrounding_text(self, input, output, processor):
        assert processor.process(input) == output
