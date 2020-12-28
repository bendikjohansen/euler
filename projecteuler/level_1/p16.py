def power_digit_sum(number: int) -> int:
    return sum([int(digit) for digit in str(number)])

if __name__ == "__main__":
    print(power_digit_sum(2**1000))
