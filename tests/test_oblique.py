import pytest

from .base import BaseTest


class TestObliqueISuffix(BaseTest):
    """Tests for î suffix oblique rule."""

    rule_name = "oblique_î_suffix+aux"

    def test_welet_to_welati(self, oblique_processor):
        text = "Ji her derê welêt heval hebûn û ez baş pê hisiyam ku hemû kurmanc wekî hev napeyivin, heman peyvan bi kar nayînin û devokên zimanê me jî hene."
        expected = "Ji her derê welatî heval hebûn û ez baş pê hisiyam ku hemû kurmanc wekî hev napeyivin, heman peyvan bi kar nayînin û devokên zimanê me jî hene."
        assert oblique_processor.process(text) == expected

    def test_welet_e_to_welati_ye(self, oblique_processor):
        text = "Her weha li gel wî li derveyî welêt rewşenbîrê bi navê Massimo Ciaravolo jî heman xelat girt ku ev xelat jî danasîna welêt e li derveyî Swêdê."
        expected = "Her weha li gel wî li derveyî welatî rewşenbîrê bi navê Massimo Ciaravolo jî heman xelat girt ku ev xelat jî danasîna welatî ye li derveyî Swêdê."
        assert oblique_processor.process(text) == expected

    def test_welet_in_to_welati_ne(self, oblique_processor):
        text = "9 kesên ku cezayên wan hatine erêkirin û hê jî li dervayê welêt in û ji bo wan jî doz demborî dibe."
        expected = "9 kesên ku cezayên wan hatine erêkirin û hê jî li dervayê welatî ne û ji bo wan jî doz demborî dibe."
        assert oblique_processor.process(text) == expected

    def test_diwer_to_diwari(self, oblique_processor):
        text = "televizyon dikare li ser dîwer were bicihkirin!"
        expected = "televizyon dikare li ser dîwarî were bicihkirin!"
        assert oblique_processor.process(text) == expected

    def test_zimen_to_zimani(self, oblique_processor):
        text = "Eger di wan de nebin îcar pêwîst dike mirov alîkariyê ji saziyên xwe yên zimên û kesên eleqedar û pêewle bixwaze"
        expected = "Eger di wan de nebin îcar pêwîst dike mirov alîkariyê ji saziyên xwe yên zimanî û kesên eleqedar û pêewle bixwaze"
        assert oblique_processor.process(text) == expected

    def test_zimen_e_to_zimani_ye(self, oblique_processor):
        text = "Yek ji armancên wê yên sereke jî perwerdeya zimên e û ew bi xwe rêzikparêz e ku tevahiya rêzikên zimanekî jî li xwe vedihewîne"
        expected = "Yek ji armancên wê yên sereke jî perwerdeya zimanî ye û ew bi xwe rêzikparêz e ku tevahiya rêzikên zimanekî jî li xwe vedihewîne"
        assert oblique_processor.process(text) == expected

    def test_zimen_in_to_zimani_ne(self, oblique_processor):
        text = "Ji ber vê em parçeyekî zimên in û paşê jî em dibin navgîna zimên."
        expected = "Ji ber vê em parçeyekî zimanî ne û paşê jî em dibin navgîna zimanî."
        assert oblique_processor.process(text) == expected

    def test_bajer_to_bajari(self, oblique_processor):
        text = "Bi vê cure hilbijartina hanê li bajar, bajarok û qesebeyan şaredar (seroka/ê belediyeyê), meclisa şaredariyê (belediyeyê) û endamên meclisa giştî ya bajêr tên diyarkirin."
        expected = "Bi vê cure hilbijartina hanê li bajar, bajarok û qesebeyan şaredar (seroka/ê belediyeyê), meclisa şaredariyê (belediyeyê) û endamên meclisa giştî ya bajarî tên diyarkirin."
        assert oblique_processor.process(text) == expected

    def test_bajer_im_to_bajari_me(self, oblique_processor):
        text = "Ez tevahiya rojê li bajêr im"
        expected = "Ez tevahiya rojê li bajarî me"
        assert oblique_processor.process(text) == expected

    def test_bajer_e_to_bajari_ye(self, oblique_processor):
        text = "Her wiha di mehên zivistanê de hema hema yek ji deverên herî sar ên bajêr e."
        expected = "Her wiha di mehên zivistanê de hema hema yek ji deverên herî sar ên bajarî ye."
        assert oblique_processor.process(text) == expected

    def test_bajer_in_to_bajari_ne(self, oblique_processor):
        text = "Kujerên wan jî li nava bajêr in"
        expected = "Kujerên wan jî li nava bajarî ne"
        assert oblique_processor.process(text) == expected

    def test_egir_to_agiri(self, oblique_processor):
        text = "Pîrozbahî gelek caran li dora êgir tê girtin, stran û dîlan tên gotin."
        expected = (
            "Pîrozbahî gelek caran li dora agirî tê girtin, stran û dîlan tên gotin."
        )
        assert oblique_processor.process(text) == expected

    def test_egir_im_to_agiri_me(self, oblique_processor):
        text = "Nameyeke ji êgir im îro di himbêza diya xwe de li berrîya Mêrdînê"
        expected = "Nameyeke ji agirî me îro di himbêza diya xwe de li berrîya Mêrdînê"
        assert oblique_processor.process(text) == expected

    def test_egir_e_to_agiri_ye(self, oblique_processor):
        text = "Dîroka çapemeniya azad herçiqas tijî serkeftin û serfirazî be jî, herwiha dîrokeke ji êgir e jî."
        expected = "Dîroka çapemeniya azad herçiqas tijî serkeftin û serfirazî be jî, herwiha dîrokeke ji agirî ye jî."
        assert oblique_processor.process(text) == expected

    def test_mest_e_to_masti_ye(self, oblique_processor):
        text = "Bila Kurdistan tev bi dirûşmeya JIN, JIYAN, AZADÎ bixemilê, da neyar bibîne dew birayê mêst e"
        expected = "Bila Kurdistan tev bi dirûşmeya JIN, JIYAN, AZADÎ bixemilê, da neyar bibîne dew birayê mastî ye"
        assert oblique_processor.process(text) == expected

    def test_cem_to_cemi(self, oblique_processor):
        text = "Li gor hin çavkaniyên kevin tê gotin ku ev masî berê ne di nav golê de, tenê li ber çêm û rûbarên ku diherikin golê de jiyan dikirin."
        expected = "Li gor hin çavkaniyên kevin tê gotin ku ev masî berê ne di nav golê de, tenê li ber çêm û rûbarên ku diherikin golê de jiyan dikirin."
        assert oblique_processor.process(text) == expected

    def test_nen_to_nani(self, oblique_processor):
        text = "Bi taybetî giringîya manewî ya tenûr û kuçikan di jîyana gund û taxan de ev cureyên nên kirîye semboleka çandî ya kurdan"
        expected = "Bi taybetî giringîya manewî ya tenûr û kuçikan di jîyana gund û taxan de ev cureyên nanî kirîye semboleka çandî ya kurdan"
        assert oblique_processor.process(text) == expected

    def test_nen_e_to_nani_ye(self, oblique_processor):
        text = "Li gorî çalakvanan pirsgirêk ne bi tenê nirxê nên e, lê kiwalîtiya wî jî gelek xerab e."
        expected = "Li gorî çalakvanan pirsgirêk ne bi tenê nirxê nanî ye, lê kiwalîtiya wî jî gelek xerab e."
        assert oblique_processor.process(text) == expected

    def test_nen_in_to_nani_ne(self, oblique_processor):
        text = "Serokê Giştî yê EMEP'ê Ercument Akdenîz jî got ku mirov muhtacî nên in û nikarin goşt û şîr bikirin."
        expected = "Serokê Giştî yê EMEP'ê Ercument Akdenîz jî got ku mirov muhtacî nanî ne û nikarin goşt û şîr bikirin."
        assert oblique_processor.process(text) == expected

    def test_genim_to_genimi(self, oblique_processor):
        text = "Heya ku ew sap baş hûr dibû, firîkên cê û gênim ji hev berdidan."
        expected = "Heya ku ew sap baş hûr dibû, firîkên cê û genimî ji hev berdidan."
        assert oblique_processor.process(text) == expected

    def test_xeni_to_xaniyi(self, oblique_processor):
        text = "Şevê, ronahiya heyvê dabûye hundirê xênî"
        expected = "Şevê, ronahiya heyvê dabûye hundirê xanîyî"
        assert oblique_processor.process(text) == expected

    def test_siven_to_sivani(self, oblique_processor):
        text = "Wekî tu bêjî çiyayan volkanên xwe teqandin, her jinekê şivên di destê xwe de hilgirtin û êrîşî ser zilam kirin û tiştek di wan de nehîştin."
        expected = "Wekî tu bêjî çiyayan volkanên xwe teqandin, her jinekê şivanî di destê xwe de hilgirtin û êrîşî ser zilam kirin û tiştek di wan de nehîştin."
        assert oblique_processor.process(text) == expected

    def test_siven_e_to_sivani_ye(self, oblique_processor):
        text = "Dawet tê kirin û berbû tên ku keçikê bibin zozanekî din, lê ji nişkê ve dengê bilûrekê ku dilê mirov zîz dike tê û ev deng ê bilûra şivên e."
        expected = "Dawet tê kirin û berbû tên ku keçikê bibin zozanekî din, lê ji nişkê ve dengê bilûrekê ku dilê mirov zîz dike tê û ev deng ê bilûra şivanî ye."
        assert oblique_processor.process(text) == expected

    def test_dermen_to_dermani(self, oblique_processor):
        text = "Kesekî ku nexweş dikeve, tûşî şobekê yan zikêşekê yan her nexweşiya din dibe, diçe ba bijîşk û piştî wergirtina dermên bi rojekê yan hefteyekê yan mehekê baş dibe."
        expected = "Kesekî ku nexweş dikeve, tûşî şobekê yan zikêşekê yan her nexweşiya din dibe, diçe ba bijîşk û piştî wergirtina dermanî bi rojekê yan hefteyekê yan mehekê baş dibe."
        assert oblique_processor.process(text) == expected

    def test_dermen_in_to_dermani_ne(self, oblique_processor):
        text = "Serbar kir, kargeh dermên bi şêweyekî dizî û nirxekî giran difroşin dermanxaneyan û firqeya çaran ya ser bi rêjma Sûriyê ve bacên ku dighin 28% li ser dermên disepîne, ev jî ji sedemên bilindbûna nirxê dermên in."
        expected = "Serbar kir, kargeh dermanî bi şêweyekî dizî û nirxekî giran difroşin dermanxaneyan û firqeya çaran ya ser bi rêjma Sûriyê ve bacên ku dighin 28% li ser dermanî disepîne, ev jî ji sedemên bilindbûna nirxê dermanî ne."
        assert oblique_processor.process(text) == expected
