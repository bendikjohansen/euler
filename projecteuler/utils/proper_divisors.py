from typing import List, Set
from functools import reduce
from itertools import combinations
from projecteuler.utils import prime_divisors


def product_of_lists(numbers: Set[List[int]]) -> int:
    return [reduce(lambda x, y: x * y, divs, 1) for divs in numbers]


def proper_divisors(number: int, primes: List[int]) -> List[int]:
    p_divs = prime_divisors(number, primes)
    divisors = [divisor
                for l in range(1, len(p_divs) + 1)
                for divisor in combinations(p_divs, l)]
    return set(filter(lambda x: x != number, product_of_lists(set(divisors))))
