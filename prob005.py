"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from prob003 import prime_factors

def smallest_multiple(min_val, max_val):
  min_val = max(min_val, 2)
  factor_counts = dict()
  for i in range(min_val, max_val+1):
    i_factors = prime_factors(i)
    for factor in i_factors:
      i_factor_count = i_factors.count(factor)
      if factor in factor_counts:
        factor_count = max(factor_counts[factor], i_factor_count)
      else:
        factor_count = i_factor_count
      factor_counts[factor] = factor_count
  product = 1
  for factor, count in factor_counts.iteritems():
    product = product * (factor ** count)
  return product

if __name__ == "__main__":
  print smallest_multiple(1, 20)
