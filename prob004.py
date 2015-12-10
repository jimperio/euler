"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(s):
  return s == s[::-1]

def get_largest_palindrome_product():
  palindromes = set()
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i*j
      if is_palindrome(str(product)):
        palindromes.add(product)
  return max(palindromes)

if __name__ == "__main__":
  print get_largest_palindrome_product()
