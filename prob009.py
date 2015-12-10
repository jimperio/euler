"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_triplet_with_sum(target_sum):
  for a in range(1, target_sum):
    for b in range(a + 1, target_sum - a + 1):
      for c in range(b + 1, target_sum - b - a + 1):
        if (a**2 + b**2) == c**2 and a + b + c == target_sum:
          return (a, b, c)

if __name__ == "__main__":
  print reduce(lambda x,y: x*y, find_triplet_with_sum(1000))
