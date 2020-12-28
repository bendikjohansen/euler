from typing import List, Set
from itertools import combinations
from functools import reduce


def product(numbers: Set[List[int]]) -> int:
    return [reduce(lambda x, y: x * y, divs, 1) for divs in numbers]


def prime_divisors(number: int, primes: List[int]) -> List[int]:
    if number in primes:
        return [1]
    divisors = [1]
    n = number
    for i in primes:
        while n % i == 0:
            divisors.append(i)
            n //= i
    return divisors


def proper_divisors(number: int, primes: List[int]) -> List[int]:
    primes = prime_divisors(number, primes)
    divisors = [divisor
                for l in range(1, len(primes) + 1)
                for divisor in combinations(primes, l)]
    return set(filter(lambda x: x != number, product(set(divisors))))


def find_primes(limit: int) -> List[int]:
    is_prime = [False, False, True] + [True] * limit
    primes = [2]
    for i in range(3, limit, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit, 2 * i):
                is_prime[j] = False

    return primes


def has_pair(i: int, sum_of_proper_divisors: List[int]) -> bool:
    pair = sum_of_proper_divisors[i]
    if not 0 < pair < len(sum_of_proper_divisors):
        return False
    return sum_of_proper_divisors[pair] == i and pair != i


def amicable_numbers(limit: int) -> int:
    primes = find_primes(limit)
    sum_of_proper_divisors = [0] + [sum(proper_divisors(i, primes))
                              for i in range(1, limit)]

    pairs = [i for i in range(1, limit) if has_pair(i, sum_of_proper_divisors)]
    return sum(pairs)


if __name__ == "__main__":
    print(amicable_numbers(int(1e4)))
