"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a and b
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt


def get_divisors(n):
  divisors = set()
  i = 1
  while i <= sqrt(n):
    if n % i == 0:
      divisors.add(i)
      if i != n/i:
        divisors.add(n/i)
    i += 1
  return divisors

def d(n):
  divs = get_divisors(n)
  divs.discard(n)
  return sum(divs)

if __name__ == "__main__":
  nums = range(2, 10001)
  amicable_nums = set()
  while nums:
    num = nums.pop()
    x = d(num)
    if x in nums:
      if num == d(x):
        nums.remove(x)
        amicable_nums.add(num)
        amicable_nums.add(x)
  print sum(amicable_nums)
