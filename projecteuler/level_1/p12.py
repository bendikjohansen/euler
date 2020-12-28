from typing import List
from functools import reduce


def product(numbers: List[int]):
    return reduce(lambda x, y: x * y, numbers, 1)


def find_primes(limit: int) -> List[int]:
    is_prime = [False, False, True] + [True] * limit
    primes = [2]
    for i in range(3, limit, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit, 2 * i):
                is_prime[j] = False

    return primes


def count_divisors(number: int, primes: List[int]) -> List[int]:
    prime_counts = []
    rest = int(number)
    for prime in primes:
        if prime > rest:
            return product([count + 1 for count in prime_counts])

        count = 0
        while rest % prime == 0:
            count += 1
            rest //= prime
        if count > 0:
            prime_counts.append(count)
    return 0



def highly_divisible_triangular_number(expected_divisor_count: int) -> int:
    primes = find_primes(int(1e7))

    for i in range(1, int(1e7)):
        number = sum(range(i+1))
        divisors_count = count_divisors(number, primes)

        if expected_divisor_count < divisors_count:
            return number


if __name__ == "__main__":
    print(highly_divisible_triangular_number(500))
