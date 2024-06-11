#!/usr/bin/env python3
"""The module contains make multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply