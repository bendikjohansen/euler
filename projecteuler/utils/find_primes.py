from typing import List


def find_primes(limit: int) -> List[int]:
    limit = int(limit)
    is_prime = [False, False, True] + [True] * limit
    primes = [2]
    for i in range(3, limit, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit, 2 * i):
                is_prime[j] = False

    return primes
