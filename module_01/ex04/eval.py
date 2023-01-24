from typing import List


class Evaluator:
    def zip_evaluate(coeffs: List[float], words: List[str]) -> float:
        return -1 if len(words) != len(coeffs) else sum(
            len(w) * c for w, c in zip(words, coeffs)
        )

    def enumerate_evaluate(coeffs: List[float], words: List[str]) -> float:
        return -1 if len(words) != len(coeffs) else sum(
            len(w) * coeffs[i] for i, w in enumerate(words)
        )
