from kmr_standardizer.processors import PROCESSORS


def standardize(text: str) -> str:
    for processor_ins in PROCESSORS.values():
        text = processor_ins.process(text)

    return text
