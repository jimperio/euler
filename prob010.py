"""
Find the sum of all the primes below two million.
"""

from prob007 import gen_primes, find_prime

def sum_primes_up_to(n):
  total = 0
  for p in gen_primes():
    if p < n:
      total += p
    else:
      return total

if __name__ == "__main__":
  print sum_primes_up_to(2000000)
