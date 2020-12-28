def nth_prime(n):
  limit = n * 20
  is_prime = [False, False, True] + [True] * limit
  prime_count = 1
  for i in range(3, limit, 2):
    if is_prime[i]:
      prime_count += 1

      if prime_count == n:
        return i

      for j in range(i*i, limit, 2 * i):
        is_prime[j] = False

if __name__ == "__main__":
    print(nth_prime(10001))
