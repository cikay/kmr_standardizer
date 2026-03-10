import re

from .base import Processor
from kmr_standardizer.models import Rule, CategoryTypes, Example


class PrepositionProcessor(Processor):
    rules = [
        Rule(
            pattern=r"\bde\b",
            replacement="da",  # replace de with da
            category=CategoryTypes.PREPOSITION,
            examples=[
                Example(
                    input="Berî çend salan, muzîka kurdî bi piranî di nav malbatan de, di dawetan de an jî di radyoyan de dihat guhdarîkirin.",
                    output="Berî çend salan, muzîka kurdî bi piranî di nav malbatan da, di dawetan da an jî di radyoyan da dihat guhdarîkirin.",
                )
            ],
        ),
        Rule(
            pattern=r"\bre\b",
            replacement="ra",  # replace re with ra
            category=CategoryTypes.PREPOSITION,
            examples=[
                Example(
                    input="Ji zarokatîyê ve bi muzîkê re eleqedar e, li sala 1991an çûye Stenbolê û bi koma birayê xwe Çîya re dest bi stranbêjîyê kirîye",
                    output="Ji zarokatîyê ve bi muzîkê ra eleqedar e, li sala 1991an çûye Stenbolê û bi koma birayê xwe Çîya ra dest bi stranbêjîyê kirîye",
                )
            ],
        ),
    ]

    def process(self, text: str) -> str:
        for rule in self.rules:
            text = re.sub(rule.pattern, rule.replacement, text)
        return text
