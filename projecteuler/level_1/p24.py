from itertools import permutations


def lexicographic_permutations(n: int) -> int:
    return ''.join(map(str, list(permutations(range(10), 10))[n + 1]))


if __name__ == "__main__":
    print(lexicographic_permutations(1000000))
