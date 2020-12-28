from functools import reduce


def factorial_digit_sum(n: int) -> int:
    number = reduce(lambda x, y: x * y, range(1, n + 1), 1)
    digits = [int(digit) for digit in str(number)]
    return sum(digits)


if __name__ == "__main__":
    print(factorial_digit_sum(100))
