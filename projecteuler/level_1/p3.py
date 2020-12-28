from math import sqrt

def divide_by(num, divisor):
  while num % divisor == 0:
    num /= divisor
  return num

def largest_prime_in(num):
  if num == 0:
    return 0

  divided = divide_by(num, 2)
  if divided == 0:
    return 2

  for i in range(3, int(sqrt(num)), 2):
    divided = divide_by(divided, i)
    if divided == 1:
      return i

  return num

if __name__ == "__main__":
    print(largest_prime_in(600851475143))
