def solve(a, b, limit):
  a_sum = sum(range(a, limit, a))
  b_sum = sum(range(b, limit, b))
  ab_sum = sum(range(a * b, limit, a * b))
  return a_sum + b_sum - ab_sum

if __name__ == "__main__":
    print(solve(3, 5, 1000))
