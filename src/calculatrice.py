from __future__ import annotations


def division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return float(a / b)


def puissance(a: float, n: int) -> float:
    if n < 0:
        raise ValueError("Exposant négatif non autorisé")
    return float(a ** n)


def moyenne(notes: list[float]) -> float:
    if len(notes) == 0:
        raise ValueError("Liste vide")
    return float(sum(notes) / len(notes))