from math import sqrt


def special_pythagorean_triplet(expected_sum: int) -> int:
    for n in range(50):
        for m in range(n + 1, 50):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if a + b + c == expected_sum:
                return a * b * c


if __name__ == "__main__":
    print(special_pythagorean_triplet(1000))
