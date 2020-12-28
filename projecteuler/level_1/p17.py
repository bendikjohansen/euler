def number_letter_counts() -> int:
    numbers = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'onethousand'
    }

    count = 0
    for number in range(1, 1001):
        digits = [int(digit) for digit in str(number)]
        if len(digits) >= 2 and 10 < number % 100 < 20:
            one = numbers[number % 100]
            ten = ''
        else:
            one = numbers[digits[-1]] if digits[-1] != 0 else ''
            ten = numbers[digits[-2] *
                          10] if len(digits) >= 2 and digits[-2] != 0 else ''
        hundred = f'{numbers[digits[-3]]}{numbers[100]}' if len(
            digits) == 3 else ''
        thousand = numbers[digits[-4] * 1000] if len(digits) == 4 else ''
        bind = 'and' if hundred != '' and (ten != '' or one != '') else ''
        spoken = f'{thousand}{hundred}{bind}{ten}{one}'

        count += len(spoken)

    return count


if __name__ == "__main__":
    print(number_letter_counts())
