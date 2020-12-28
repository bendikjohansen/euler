def sum_square_difference(limit):
  sum_of_squares = sum([x ** 2 for x in range(1, limit + 1)])
  square_of_sums = sum(range(1, limit + 1)) ** 2
  return square_of_sums - sum_of_squares

if __name__ == "__main__":
    print(sum_square_difference(100))
