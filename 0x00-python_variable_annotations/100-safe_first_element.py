#!/usr/bin/env python3
"""
Safe first element
"""
from typing import Any, Union


def safe_first_element(lst: Any) -> Union[Any, None]:
    """safe_first_element"""

    if lst:
        return lst[0]
    else:
        return None
