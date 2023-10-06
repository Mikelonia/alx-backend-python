#!/usr/bin/env python3
'''Task 5's module.
'''
from typing import List

def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of a list of floating-point numbers.
    '''
    return sum(input_list)

# Example usage:
result: float = sum_list([1.5, 2.0, 3.5])
print(result)

