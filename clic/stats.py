"""Corpus Statistics."""

import math


def zscore(nOccsCorpus, nOccsSection, sizeCorpus, sizeSection):
    "Caclulate and return z-score."
    O = float(nOccsSection)
    p = float(nOccsCorpus) / float(sizeCorpus)
    E = float((p) * sizeSection)
    sigma = math.sqrt(sizeSection * (p * (1 - p)))
    z = (O - E) / sigma
    return z
