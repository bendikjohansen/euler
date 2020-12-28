from typing import List, Set
from itertools import combinations
from functools import reduce
from projecteuler.utils import proper_divisors, find_primes

def non_abundant_sums() -> int:
    limit = 28123
    primes = find_primes(limit)
    abundant_numbers = [n for n in range(1, limit) if sum(proper_divisors(n, primes)) > n]

    sum_of_pairs = set()
    for n in abundant_numbers:
        for m in abundant_numbers[abundant_numbers.index(n):]:
            sum_of_pairs.add(n + m)

    return sum(filter(lambda x: x not in sum_of_pairs, range(1, limit + 1)))


if __name__ == "__main__":
    print(non_abundant_sums())
