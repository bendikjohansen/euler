from typing import List


def find_primes(limit: int) -> List[int]:
    is_prime = [False, False, True] + [True] * limit
    primes = [2]
    for i in range(3, limit, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit, 2 * i):
                is_prime[j] = False

    return primes


def summation_of_primes(limit: int) -> int:
    return sum(find_primes(limit))


if __name__ == "__main__":
    print(summation_of_primes(int(2e6)))
