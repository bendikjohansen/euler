def is_palindrome(number: int) -> bool:
  return str(number) == str(number)[::-1]

def largest_palindrome():
  palindromes = []
  min_num, max_num = int(1e2), int(1e3)
  for i in range(min_num, max_num):
    for j in range(min_num, max_num):
      if is_palindrome(i * j):
        palindromes.append(i * j)

  return max(palindromes)

if __name__ == "__main__":
    print(largest_palindrome())
