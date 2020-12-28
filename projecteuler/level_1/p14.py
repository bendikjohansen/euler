from typing import Dict


def collatz_sequence(n: int, sequences: Dict = {}) -> int:
    if n == 1:
        return 1

    if n not in sequences:
        next_n = int(n / 2 if n % 2 == 0 else 3*n + 1)
        length = collatz_sequence(next_n, sequences)
        sequences[n] = length + 1

    return sequences[n]


def longest_collatz_sequence(limit: int) -> int:
    lengths = {}
    for i in range(1, limit):
        collatz_sequence(i, lengths)
    return max(lengths, key=lambda key: lengths[key])

if __name__ == "__main__":
    print(longest_collatz_sequence(int(1e6)))
