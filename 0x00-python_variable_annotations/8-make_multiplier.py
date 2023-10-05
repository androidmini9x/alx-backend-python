#!/usr/bin/env python3
'''8. Complex types - functions
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return func that multiplies a float by multiplier'''
    def _(x: float) -> float:
        return x * multiplier
    return _
