from projecteuler.utils import get_input

def names_scores(names_raw: str) -> int:
    names = names_raw.replace('"', '').split(',')
    names.sort()
    alphabetical_values = [sum([ord(letter) - ord('A') + 1 for letter in name]) for name in names]
    return sum(value * (index + 1) for index, value in enumerate(alphabetical_values))


if __name__ == "__main__":
    names_raw = get_input(22)
    print(names_scores(names_raw))
