"""scrabble-score-fn-score-conformance-oracle -- deterministic CONFORMANCE oracle for `scrabble-score` (python).

WHAT THIS DECIDES: given a candidate callable and one canonical input, it decides whether the candidate
agrees with the proven reference. It is a *conformance* decider over a fixed, published corpus -- it does
not decide correctness in general, and it says nothing about inputs outside the corpus.

SCOPE (declared, so the boundary is visible rather than discovered): the corpus is the canonical Exercism
test data for this task, 8 input/output pairs, listed in `probes/probes.jsonl`. Inputs outside that
set are simply not covered; `decide` answers only about the input it is given.

PROVENANCE: the reference body comes from the Exercism reference solution for `scrabble-score` (MIT, Exercism);
the type annotations were added by harvest, the body is unchanged (checked at AST level). The capability
was PROVEN by the exercism testsuite (pin=1fd1ff97f9f7c7ff) and re-executed by harvest in a sealed sandbox
(unshare -rn) -- verify-not-relay, not a copied ledger label.
"""

TASK = "scrabble-score"
CWE = "scrabble-score"          # a publish-motor egyseges mezonevet var; itt a feladat azonositoja


def decide(fn, value, expect):
    """PASS iff fn(value) == expect. Determinista, nincs halozat, nincs allapot."""
    try:
        return "PASS" if fn(value) == expect else "FAIL"
    except Exception:                                      # noqa: BLE001
        return "FAIL"


POINTS = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

def score(word: str) -> int:
    if not word.isalpha():
        return 0
    return sum((POINTS[letter] for letter in word.lower()))

REFERENCE = score
