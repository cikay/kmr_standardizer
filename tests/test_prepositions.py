import pytest

from kmr_standardizer.processors.prepositions import PrepositionProcessor


@pytest.fixture
def processor():
    original_rules = PrepositionProcessor.rules
    PrepositionProcessor.rules = [
        r for r in original_rules if r.name == "di...de->di...da"
    ]
    yield PrepositionProcessor()
    PrepositionProcessor.rules = original_rules


class TestDiDeToDiDa:
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

    def test_comma_between_di_de(self, processor):
        text = """"
        Di cureyên berhemên wêjeya devkî de, di qalib, biwêj û gotinên pêşiyan de, di bêjeyên darêştî û yên hevedudanî de bi awayekî fosîlîzebûyî şêweyên kevn, form û morfemên kevnare yên hêvişandî tên dîtin ku ew ji bo peyitandina vê yekê çavkaniyên hêja ne.
        """
        expected = """"
        Di cureyên berhemên wêjeya devkî da, di qalib, biwêj û gotinên pêşiyan da, di bêjeyên darêştî û yên hevedudanî da bi awayekî fosîlîzebûyî şêweyên kevn, form û morfemên kevnare yên hêvişandî tên dîtin ku ew ji bo peyitandina vê yekê çavkaniyên hêja ne.
        """
        assert processor.process(text) == expected

    def test_dot_between_di_de(self, processor):
        text = "Miheme Salihê Beynatî, sala 1938’an li gundê Beynata Farqînê hatiye dinyayê û di 19.05.1984’an de jî di ciwaniya xwe de xatirê xwe ji me xwast û serê xwe danî ser axa sar."
        expected = "Miheme Salihê Beynatî, sala 1938’an li gundê Beynata Farqînê hatiye dinyayê û di 19.05.1984’an da jî di ciwaniya xwe da xatirê xwe ji me xwast û serê xwe danî ser axa sar."
        assert processor.process(text) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            (
                "Di kirmanckî/zazakî de ew “merdene” û di kurmanciya naverast (soranî) de jî “mirdin” e.",  # / ( ) are in between
                "Di kirmanckî/zazakî da ew “merdene” û di kurmanciya naverast (soranî) da jî “mirdin” e.",
            ),
            (
                "Di hejmara 17’an a kovara Pîneyê (1-15 Tîrmeh 2000) de, li rûpela 5’an, bi îmzaya A. Çîçek, ku ez ne şaş bim ew Dogan Guzelê danerê Qirix bû, karîkatureke qerfî li ser vê rewşa min xêz kiribû",  # - ( ) chars are allowed
                "Di hejmara 17’an a kovara Pîneyê (1-15 Tîrmeh 2000) da, li rûpela 5’an, bi îmzaya A. Çîçek, ku ez ne şaş bim ew Dogan Guzelê danerê Qirix bû, karîkatureke qerfî li ser vê rewşa min xêz kiribû",
            ),
        ],
    )
    def test_special_chars_between_di_de(self, input, expected, processor):
        assert processor.process(input) == expected

    @pytest.mark.parametrize(
        "input,output",
        [
            (
                "di destê min de çi heye?",
                "di destê min da çi heye?",
            ),
            ("dengê xalê min", "dengê xalê min"),
        ],
    )
    def test_does_not_replace_inside_words(self, input, output, processor):
        """'de' inside words like should not be replaced."""
        assert processor.process(input) == output

    @pytest.mark.parametrize(
        "input,output",
        [
            (
                "Alex De Souza lîstikvanekî futbolê yê Brezîlî yê berê ye, niha jî teknîk direktor e",
                "Alex De Souza lîstikvanekî futbolê yê Brezîlî yê berê ye, niha jî teknîk direktor e",
            ),
        ],
    )
    def test_does_not_replace_de_in_proper_nouns(self, input, output, processor):
        # note: cannot handle the following sentence properly
        # Kûçikê me di xaniyê terikandî yê Alex De Souza de hat dîtin
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

    def test_multiline_text(self, processor):
        input = """
            – Kontrola kêzik û parazîtan: Di genim û bîberan de kêzikan tune dike, bermayîyê %20-30 kêm dike.
            – Parastina nirxê xwarinê: Di vîtamîna C û hêmanên hesas de windabûneka pir kêm çêdibe; carinan jî enzîman asteng dike û xwarinê diparêze.
            – Bikaranîna çopên nukleerî: Çavkanîyên kevn ên tibî yên nukleerî (kobalt-60) bi vî awayî ji nû ve têne bikaranîn.
            Li gorî raporanên IAEA yên 2025an, tîrêjkirin bi kêmkirina bermayîya xwarinê ji birçîbûnê re jî dibe alîkar; bi taybetî li welatên di asta pêşveçûnê de.
            Li Tirkîyeyê jî ji sala 1999an ve bi du tesîsan ev rêbaz tê bikaranîn û di sektorên goşt û biharatê de bandorê zêde dike.
        """

        output = """
            – Kontrola kêzik û parazîtan: Di genim û bîberan da kêzikan tune dike, bermayîyê %20-30 kêm dike.
            – Parastina nirxê xwarinê: Di vîtamîna C û hêmanên hesas da windabûneka pir kêm çêdibe; carinan jî enzîman asteng dike û xwarinê diparêze.
            – Bikaranîna çopên nukleerî: Çavkanîyên kevn ên tibî yên nukleerî (kobalt-60) bi vî awayî ji nû ve têne bikaranîn.
            Li gorî raporanên IAEA yên 2025an, tîrêjkirin bi kêmkirina bermayîya xwarinê ji birçîbûnê re jî dibe alîkar; bi taybetî li welatên di asta pêşveçûnê da.
            Li Tirkîyeyê jî ji sala 1999an ve bi du tesîsan ev rêbaz tê bikaranîn û di sektorên goşt û biharatê da bandorê zêde dike.
        """
        assert processor.process(input) == output


@pytest.fixture
def te_de_processor():
    original_rules = PrepositionProcessor.rules
    PrepositionProcessor.rules = [r for r in original_rules if r.name == "tê de->tê da"]
    yield PrepositionProcessor()
    PrepositionProcessor.rules = original_rules


class TestTeDeToTeDa:
    """Tests for tê de → tê da preposition rule."""

    def test_simple_replacement(self, te_de_processor):
        text = "bi her awayî ve raboriya me jî tê de ye"
        expected = "bi her awayî ve raboriya me jî tê da ye"
        assert te_de_processor.process(text) == expected

    def test_multiple_whitespace_between_them(self, te_de_processor):
        text = "li jêrê nivîsî, ku tê   de jî awayê “mirt”ê derbas dibe"
        expected = "li jêrê nivîsî, ku tê da jî awayê “mirt”ê derbas dibe"
        assert te_de_processor.process(text) == expected


@pytest.fixture
def ji_de_processor():
    original_rules = PrepositionProcessor.rules
    PrepositionProcessor.rules = [r for r in original_rules if r.name == "ji...de->ji...da"]
    yield PrepositionProcessor()
    PrepositionProcessor.rules = original_rules


class TestJiDeToJiDa:
    """Tests for ji ... de → ji ... da preposition rule."""

    def test_simple_replacement(self, ji_de_processor):
        text = "Erê, hişmendiya piraniyê jinan ji vî alî de bihêz e, ne weke berê ye."
        expected = (
            "Erê, hişmendiya piraniyê jinan ji vî alî da bihêz e, ne weke berê ye."
        )
        assert ji_de_processor.process(text) == expected

    def test_does_not_replace_when_di_between_ji_de(self, ji_de_processor):
        text = "Tevgerîna bi awayê berpirsane divê ji bo me giştan rêbaza sereke be û em hewl bidin terman rast û di cih de bi kar bînin."
        assert ji_de_processor.process(text) == text

    def test_does_not_replace_when_bi_between_ji_de(self, ji_de_processor):
        text = "Tiştê ji xwe re heq dibîne, ji yên din re nabîne, tiştê ji xwe re sedema berdewamiya hebûna xwe dibîne, ji bo yên din nabîne, tew bi ser de wan ji xwe re talûke jî dihesibîne."
        assert ji_de_processor.process(text) == text

    def test_does_not_replace_when_der_heqe_between_ji_de(self, ji_de_processor):
        text = "Di serî de bibêjim ku derdê min ne ew e ez ji aliyê zanistî ve li ser têkiliya mêjî û zimên bisekinim û der heqê xewnan û binhişê mirov de jî analîzên psîkolojîk bikim."
        assert ji_de_processor.process(text) == text

    def test_does_not_replace_when_derheqe_between_ji_de(self, ji_de_processor):
        "ji .. derheqê ... de"
        text = "Ji xeynî van tabletan derheqê cebîr û geometrîyê de jî tablet hatine dîtin."
        assert ji_de_processor.process(text) == text

    def test_does_not_replace_when_der_bare_between_ji_de(self, ji_de_processor):
        "ji .. der barê ... de"
        text = "Herçî berhema Dionysios “Tekhne Grammatike” ye, ji bilî hevoksaziyê (sentaksê), der barê hemû mijarên zimên de 13 qirn wek deqeke hîmî li Rojava hatiye pejirandin"
        assert ji_de_processor.process(text) == text

    def test_does_not_replace_when_derbare_between_ji_de(self, ji_de_processor):
        "ji .. derbarê ... de"
        text = "Di heman demê de, ji sala 2014an vir ve li beşa Ziman û Çanda Kurdî ya zanîngeha Mêrdînê çend tezên Masterê yên derbarê Şahnameyên Kurdî de hatine amade kirin û têne amade kirin"
        assert ji_de_processor.process(text) == text

    def test_does_not_replace_when_te_between_ji_de(self, ji_de_processor):
        "ji .. tê ... de"
        text = "Min îsal jî li Wanê, ji zarê parêzera hêja Jînda Rûgeş Koçakê, ku ew ji Nordizê û ji Mamxuran e, ev a hanê ya li jêrê nivîsî, ku tê de jî awayê “mirt”ê derbas dibe."
        assert ji_de_processor.process(text) == text

    def test_does_not_replace_when_pe_between_ji_de(self, ji_de_processor):
        "ji .. pê ... de"
        text = "Hema em li van zimanan binêrin û wisan ji xwe re pê de herin û bipirsin"
        assert ji_de_processor.process(text) == text

    def test_does_not_replace_when_je_between_ji_de(self, ji_de_processor):
        "ji .. jê ... de"
        text = "We bi piştgiriya xwe ya li hember kurdan cinawirek afirand û niha ew cinawir dixwaze hinekî goştê we bixwe, ji ber ku li kurdan dev jê ber de goşt, hestî jî nemane."
        assert ji_de_processor.process(text) == text

