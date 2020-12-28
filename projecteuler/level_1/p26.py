def reciprocal_cycles(limit: int) -> int:
    longest_number = 0
    longest_reccurence = 0

    for denominator in range(2, limit):
        previous_numbers = [False] * limit
        continue_division = True
        current_number = 1
        counter = 0

        while continue_division:
            while current_number < denominator:
                current_number *= 10

            current_number %= denominator
            counter += 1

            for _ in range(1, len(previous_numbers)):
                if not continue_division:
                    break
                continue_division = not previous_numbers[current_number]

            if current_number == 0:
                continue_division = False

            previous_numbers[current_number] = True
        if longest_reccurence < counter:
            longest_reccurence = counter
            longest_number = denominator
    return longest_number



if __name__ == "__main__":
    print(reciprocal_cycles(1000))
