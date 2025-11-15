"""
TRANSITIONS: A transition is a type of nucleotide substitution where a purine is replaced by another purine (A <-> G) or a pyrimidine is replaced by another pyrimidine (C <-> T).
TRANSVERSIONS: A transversion is a type of nucleotide substitution where a purine is replaced by a pyrimidine or vice versa (A <-> C, A <-> T, G <-> C, G <-> T).
TRANSITION/TRANSVERSION RATIO: The ratio of the number of transitions to the number of transversions observed in a set of nucleotide sequences.
"""

def transition_transversion_ratio(s1, s2):
    """
    Computes the transition/transversion ratio R(s1, s2)
    for two DNA strings of equal length.
    """
    transitions = {('A','G'), ('G','A'), ('C','T'), ('T','C')}
    ti = tv = 0
    for a, b in zip(s1, s2):
        if a != b:
            if (a, b) in transitions:
                ti += 1
            else:       ## transversion = not a transition
                tv += 1
    if tv == 0:
        return float('inf')  # avoid division by zero
    return ti / tv

# Example usage:
s1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
s2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"
print(transition_transversion_ratio(s1, s2))