import pytest

from .base import BaseTest


class TestDiDeToDiDa(BaseTest):
    """Tests for di ... de → di ... da preposition rule."""

    rule_name = "di...de->di...da"

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

    def test_colon_between_di_de(self, processor):
        text = "Di 12ê Tebaxê seet 20:00-02:00an de bi şîara “balgehê xwe hilde û were” Çalakîya Barîna Meteoran dê pêk were."
        expected = "Di 12ê Tebaxê seet 20:00-02:00an da bi şîara “balgehê xwe hilde û were” Çalakîya Barîna Meteoran dê pêk were."
        assert processor.process(text) == expected

    def test_does_not_replace_de_as_proper_noun(self, processor):
        text = "Ji bilî van yekan, Ferdinand de Saussure ku ew hîmdarê zimannasiya binyadgeriyê ye, balê dikişîne aliyê fizîkî, fizyolojîk û ruhî yên melekeyên zimên û dibêje ku pêwendiya zimên bi warên ferdî û civakî re heye."
        assert processor.process(text) == text

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


class TestTeDeToTeDa(BaseTest):
    """Tests for tê de → tê da preposition rule."""

    rule_name = "tê de->tê da"

    def test_simple_replacement(self, processor):
        text = "bi her awayî ve raboriya me jî tê de ye"
        expected = "bi her awayî ve raboriya me jî tê da ye"
        assert processor.process(text) == expected

    def test_multiple_whitespace_between_them(self, processor):
        text = "li jêrê nivîsî, ku tê   de jî awayê “mirt”ê derbas dibe"
        expected = "li jêrê nivîsî, ku tê da jî awayê “mirt”ê derbas dibe"
        assert processor.process(text) == expected


class TestDerbareDerheqeDeToDerbareDerheqeDa(BaseTest):
    """Tests for derbarê/derheqê ... de ->derbarê/derheqê ... da preposition rule."""

    rule_name = "derbarê/derheqê ... de ->derbarê/derheqê ... da"

    def test_derbare_de(self, processor):
        text = "Sedema zehmetbûna diyarkirina çîrokên Şahnameyên Kurdî berî her tiştî ev e ku hejmareka nediyar ya destxetên Kurdî di kitêbxaneyên cuda yên dinyayê de di bin navê zimanekî din de hatine qeydkirin û ev yek jî bûye sedem ku vekolînên derbarê edebiyata Kurdî de bi zehmet bikevin"
        expected = "Sedema zehmetbûna diyarkirina çîrokên Şahnameyên Kurdî berî her tiştî ev e ku hejmareka nediyar ya destxetên Kurdî di kitêbxaneyên cuda yên dinyayê de di bin navê zimanekî din de hatine qeydkirin û ev yek jî bûye sedem ku vekolînên derbarê edebiyata Kurdî da bi zehmet bikevin"
        assert processor.process(text) == expected

    def test_derbare_de_multiple_space(self, processor):
        text = "derbarê  vê mijarê  de"
        expected = "derbarê  vê mijarê  da"
        assert processor.process(text) == expected

    def test_der_bare_de(self, processor):
        text = "Hestên neteweyî û helwesta axêverên wî zimanî ya der barê zimanê wan de"
        expected = (
            "Hestên neteweyî û helwesta axêverên wî zimanî ya der barê zimanê wan da"
        )
        assert processor.process(text) == expected

    def test_der_bare_de_multiple_space(self, processor):
        text = "der  barê  vê mijarê  de"
        expected = "der  barê  vê mijarê  da"
        assert processor.process(text) == expected

    def test_der_heqe_de(self, processor):
        text = "Lê bi kurtasî be jî, ez dixwazim dîsan çend gotinan der heqê vê yekê de bibêjim."
        expected = "Lê bi kurtasî be jî, ez dixwazim dîsan çend gotinan der heqê vê yekê da bibêjim."
        assert processor.process(text) == expected

    def test_der_heqe_de_multiple_space(self, processor):
        text = "der  heqê  vê mijarê  de"
        expected = "der  heqê  vê mijarê  da"
        assert processor.process(text) == expected

    def test_derheqe_de(self, processor):
        text = "Tişta gelekî balkêş a derheqê babilîyan de ev e ji bo hesabên xwe tablo çêdikirin."
        expected = "Tişta gelekî balkêş a derheqê babilîyan da ev e ji bo hesabên xwe tablo çêdikirin."
        assert processor.process(text) == expected

    def test_derheqe_de_multiple_space(self, processor):
        text = "derheqê  vê mijarê  de"
        expected = "derheqê  vê mijarê  da"
        assert processor.process(text) == expected

    # def replace_does_not_match(self):
    #     text = "Berginda vê peyvê ya din jî “der barê… de” ye ku ew jî eynî mîna wê ne xwedî standardeke nivîsînê ye."
    #     assert processor.process(text) == text


class TestBiReToBiRa(BaseTest):
    """Tests for bi ... re->bi ... ra preposition rule."""

    rule_name = "bi ... re->bi ... ra"

    def test_no_match(self, processor):
        input = "Ji bo mirov bikare bi hunerê xwe bişîre divê bi qabiliyeta xwe jî bizane."
        assert processor.process(input) == input

    @pytest.mark.parametrize(
        "input,expected",
        [
            (
                "Carinan li ser teşeyê peyvekê pirs bi mirov re çêdibin bê çima wisan lê hatiye û ketiye rewşeke din.",
                "Carinan li ser teşeyê peyvekê pirs bi mirov ra çêdibin bê çima wisan lê hatiye û ketiye rewşeke din.",
            ),
            (
                "Ez bi vê rûdana hanê ya ku li min çêbûye gelek kêfxweş im û ji ber cihekî mistesna yê Ehmedê Xanî û şahesera wî Mem û Zîna wî bi min re heye jî, ez xwe bextewer dihesibînim.",
                "Ez bi vê rûdana hanê ya ku li min çêbûye gelek kêfxweş im û ji ber cihekî mistesna yê Ehmedê Xanî û şahesera wî Mem û Zîna wî bi min ra heye jî, ez xwe bextewer dihesibînim.",
            ),
        ],
    )
    def test_bi_re_simple_replacement(self, input, expected, processor):
        assert processor.process(input) == expected

    def test_bi_re_multiple_match(self, processor):
        text = "Li hêla din, bi kurdên hişyar û polîtîk re, çendî ku ew li xwebûna xwe û her tiştê aîdî nasnameyê ne dibin xwedî jî, eger bi awayekî giştî bê gotin, hişmendî û giringiya bikaranîna zimên a di her warî de bi wan re lawaz e."
        expected = "Li hêla din, bi kurdên hişyar û polîtîk ra, çendî ku ew li xwebûna xwe û her tiştê aîdî nasnameyê ne dibin xwedî jî, eger bi awayekî giştî bê gotin, hişmendî û giringiya bikaranîna zimên a di her warî de bi wan ra lawaz e."
        assert processor.process(text) == expected


class TestJiReToJiRa(BaseTest):
    """Tests for ji ... re->ji ... ra preposition rule."""

    rule_name = "ji ... re->ji ... ra"

    @pytest.mark.parametrize(
        "input,expected",
        [
            (
                "Carinan wekî jibîrbûyî bixuyên jî, lê ew di binhiş de bi cih bûne û wan ji xwe re hêlîna xwe çêkiriye",
                "Carinan wekî jibîrbûyî bixuyên jî, lê ew di binhiş de bi cih bûne û wan ji xwe ra hêlîna xwe çêkiriye",
            ),
            (
                "Berê mirov ber bi aliyekî de didin ku heta mirov sax be li darê dinyayê êdî ew ji mirov re dibin, aqil, tecrube, şîret û rênîşander.",
                "Berê mirov ber bi aliyekî de didin ku heta mirov sax be li darê dinyayê êdî ew ji mirov ra dibin, aqil, tecrube, şîret û rênîşander.",
            ),
            (
                "Zimanê kesên ku ji civakê re serkêşiyê dikin jî bi giranî bi tirkî ye.",
                "Zimanê kesên ku ji civakê ra serkêşiyê dikin jî bi giranî bi tirkî ye."
            ),
        ],
    )
    def test_ji_re_simple_replacement(self, input, expected, processor):
        assert processor.process(input) == expected


class TestDiReToDiRa(BaseTest):
    """Tests for di ... re->di ... ra preposition rule."""

    rule_name = "di ... re->di ... ra"

    def test_di_re_simple_replacement(self, processor):
        text = "Meseleya zimanî, meseleyeke wisan e ku di ser hemû partî û rêxistinan re ye."
        expected = "Meseleya zimanî, meseleyeke wisan e ku di ser hemû partî û rêxistinan ra ye."
        assert processor.process(text) == expected


class TestPeJeTeReToDRa(BaseTest):
    """Tests for jê/pê/tê ... re->jê/pê/tê ... ra preposition rule."""

    rule_name = "jê/pê/tê ... re->jê/pê/tê ... ra"

    def test_je_re(self, processor):
        text = "Ev jî kêşeyeke me ya din e û divê jê re jî çareseriyeke rast bê dîtin."
        expected = (
            "Ev jî kêşeyeke me ya din e û divê jê ra jî çareseriyeke rast bê dîtin."
        )
        assert processor.process(text) == expected

    def test_pe_re(self, processor):
        text = "Ji ber ku ziman bi awayekî xurt êdî li nifşa nûhatî nayê veguhastin, pê re jidestçûna çanda kurdî jî, her cure zargotin jî pêk tê"
        expected = "Ji ber ku ziman bi awayekî xurt êdî li nifşa nûhatî nayê veguhastin, pê ra jidestçûna çanda kurdî jî, her cure zargotin jî pêk tê"
        assert processor.process(text) == expected

    def test_te_re(self, processor):
        text = "Tevî ku serêşî û wextê wê yê rêwingiyê hindiktir e jî tê re neçûm."
        expected = "Tevî ku serêşî û wextê wê yê rêwingiyê hindiktir e jî tê ra neçûm."
        assert processor.process(text) == expected
