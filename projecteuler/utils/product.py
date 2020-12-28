from typing import List
from functools import reduce


def product(numbers: List[int]) -> int:
    return reduce(lambda x, y: x * y, numbers, 1)
