#!/usr/bin/env python3
"""Converts an integer to a key-value pair"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Converts an integer to a key-value pair"""

    return tuple((k, v ** 2))
