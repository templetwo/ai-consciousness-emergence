import math
from collections import Counter
import numpy as np

def low_entropy(text: str, thresh_bits: float = 3.5) -> bool:
    toks = text.split()
    total = len(toks)
    if total < 20:
        return False
    freqs = Counter(toks).values()
    H = -sum(c/total * math.log2(c/total) for c in freqs)
    return H < thresh_bits

# Placeholder for semantic_drift in environments without sentence_transformers
def semantic_drift(prev: str, new: str, thresh: float = 0.40) -> bool:
    return False