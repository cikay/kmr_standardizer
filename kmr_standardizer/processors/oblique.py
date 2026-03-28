from .base import Processor

from kmr_standardizer.models import Rule, CategoryTypes

mapping = {
    "welêt": "welatî",
    "dîwer": "dîwarî",
    "zimên": "zimanî",
    "bajêr": "bajarî",
    "êgir": "agirî",
    "mêst": "mastî",
    "nên": "nanî",
    "gênim": "genimî",
    "xênî": "xanîyî",
    "şivên": "şivanî",
    "dermên": "dermanî"
    # "zemên": "zemanî" zem-ên regex limit hits it cannot detect if the word is zem or zeman
}

aux_verb_mapping = {
    "im": "me",
    "î": "yî",
    "e": "ye",
    "in": "ne",
}

regex = "|".join(
    mapping.keys()
)


def oblique_replacement(match):
    word = match.group(1)
    aux = match.group(3)
    standard_form = mapping[word]
    if aux:
        return f"{standard_form} {aux_verb_mapping[aux]}"
    return standard_form


class ObliqueProcessor(Processor):
    rules = [
        Rule(
            pattern=rf"\b({regex})\b(\s(im|î|e|in)\b)?",
            replacement=oblique_replacement,
            name="oblique_î_suffix+aux",
            category=CategoryTypes.OBLIQUE,
        )
    ]
