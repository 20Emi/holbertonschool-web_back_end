#!/usr/bin/env python3
"""Task 8"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """main function"""

    def multiplier_funtion(val_mul: float) -> float:
        """ internal function multiplier_function
        to be returned by make_multiplier"""

        return val_mul * multiplier
    return multiplier_funtion
