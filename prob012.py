"""
What is the value of the first triangle number to have over five hundred divisors?
"""

import itertools
from math import factorial

from prob003 import prime_factors


def find_triangle_number_with_divisors(num):
  max_ds = None
  for i in gen_triangle_numbers():
    ds = len(get_divisors(i))
    if ds > num:
      return i
    if not max_ds or ds > max_ds:
      max_ds = ds
      print ds

def gen_triangle_numbers():
  i = j = 1
  while True:
    i += 1
    j += i
    yield j

# Initial working attempt.
# For this case, it took 300+ seconds!
def get_divisors(number):
  ps = prime_factors(number)
  divisors = set(ps)
  divisors.add(1)
  l = 2
  while l <= len(ps):
    for c in itertools.combinations(ps, l):
      divisors.add(reduce(lambda x, y: x * y, c))
    l += 1
  return divisors

# WIP: Derive number of divisors from number of prime factors.
# Not sure yet how to deal with duplicates, i.e.,
# for 180, prime factors are [2, 2, 3, 3, 5]
def count_divisors(number):
  num_ps = len(prime_factors(number))
  num_divisors = 1
  for k in range(1, num_ps+1):
    num_divisors += num_combinations(num_ps, k)
  return num_divisors

def num_combinations(n, k):
  return factorial(n) / (factorial(n - k) * factorial(k))

if __name__ == "__main__":
  print find_triangle_number_with_divisors(500)
