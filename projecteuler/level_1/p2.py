def even_fib_sum(limit):
  a, b, c = 0, 1, 0
  sum = 0
  while a < limit:
    c = a
    a += b
    b = c

    sum += a if a % 2 == 0 else 0
  return sum

if __name__ == "__main__":
    print(even_fib_sum(4e6))
