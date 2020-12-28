from typing import List


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
