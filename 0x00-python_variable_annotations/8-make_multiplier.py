#!/usr/bin/env python3
'''Task 8's module. By Okpako Michael
'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
