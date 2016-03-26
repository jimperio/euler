"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
5, 6, 7, 8 and 9?
"""

from math import factorial


digits = "0123456789"

def num_permutations(items):
  return factorial(len(items))

def get_nth_permutation(n, items):
  n -= 1 # Index is zero-based
  source = list(items)
  nth_permutation = ''
  # We want to get the coefficients in the expansion
  #
  #   n = a * i! + b * (i - 1)! + ... + z * 1!
  #
  # where i = (number of items) - 1.
  #
  # Let's say we have a set of 3 digits, 012, with permutations as listed above.
  # For n = 5, we get the expansion
  #
  #   n = 5 = a * 2! + b * 1! = 2 * 2! + 1 * 1!
  #
  # Intuitively, if a = 2, then we can say that we've already gone through two
  # set of permutations of the last 2 digits. This means that we've exhausted
  # the permutations beginning with 0 (the lexicographically-first element),
  # and 1 (the lexicographically-second element), hence the first item of the
  # permutation must be the lexicographically- next element, which is 2:
  #
  #   (n = 5) permutation: 2??
  #   remaining digits: 01
  #
  # Now since b = 1, we know that we've gone through one set of permutations
  # of the last digit. So we've gone through the permutation with 0 as its 2nd
  # item, and the 2nd item must be 1:
  #
  #   (n = 5) permutation: 21?
  #   remaining digit: 0
  #   --> (n = 5)th / 6th permutation is 210
  #
  i = len(items) - 1
  while i > 0:
    x, n = divmod(n, factorial(i))
    c = source.pop(x)
    nth_permutation += c
    i -= 1
  nth_permutation += source.pop()
  return nth_permutation

if __name__ == "__main__":
  print get_nth_permutation(1000000, digits)
