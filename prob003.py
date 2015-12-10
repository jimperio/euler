"""
What is the largest prime factor of the number 600851475143?
"""

def prime_factors(number):
  primes = set([2])
  prime_factors = []
  value = number
  while value % 2 == 0:
    value /= 2
    prime_factors.append(2)
  i = 3
  while i <= value:
    is_prime = True
    for k in primes:
      if i % k == 0:
        is_prime = False
        i += 2
    if is_prime:
      primes.add(i)
      while value % i == 0:
        # Found a prime factor! We can now factor it out.
        value /= i
        prime_factors.append(i)
  assert reduce(lambda x, y: x*y, prime_factors) == number
  return prime_factors

if __name__ == "__main__":
  print max(prime_factors(600851475143))
