from .prepositions import PrepositionProcessor
from .oblique import ObliqueProcessor
from kmr_standardizer.models import CategoryTypes

PROCESSORS = {
    CategoryTypes.PREPOSITION: PrepositionProcessor(),
    CategoryTypes.OBLIQUE: ObliqueProcessor(),
}
