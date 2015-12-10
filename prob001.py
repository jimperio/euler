"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""

if __name__ == "__main__":
  print sum(
  filter(lambda i: i % 3 == 0 or i % 5 == 0,
         xrange(1,1000))
  )
