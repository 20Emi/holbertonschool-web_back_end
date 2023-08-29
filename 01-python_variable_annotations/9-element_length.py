#!/usr/bin/env python3
"""Task 9"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function’s parameters and return values
    with the appropriate types"""

    return [(i, len(i)) for i in lst]
