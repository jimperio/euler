"""
What is the 10 001st prime number?
"""

def find_prime(n):
  primes = set([2])
  val = 3
  while True:
    for k in primes:
      if val % k == 0:
        val += 2
        break
    else:
      primes.add(val)
      if len(primes) >= n:
        break
  return val

# BONUS: While looking for optimization ideas, came across this gem:
# http://code.activestate.com/recipes/117119/#c4
def gen_primes():
  yield 2
  D = {}
  q = 3
  while True:
    p = D.pop(q, None)
    if p:
      x = p + q
      while x in D: x += p
      D[x] = p
    else:
      D[q*q] = 2*q
      yield q
    q += 2

if __name__ == "__main__":
  print find_prime(10001)
