from functools import reduce

def divide(current, divisors):
  for dividor in divisors:
    if current % dividor == 0:
      current /= dividor
  return current

def smallest_multiple(num):
  divisors = []
  for i in range(1, num):
    new_divisor = int(divide(i, divisors))
    if new_divisor != 1:
      divisors.append(new_divisor)

  return reduce(lambda x, y: x * y, divisors, 1)

if __name__ == "__main__":
    print(smallest_multiple(20))
