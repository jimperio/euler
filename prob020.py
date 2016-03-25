"""
Find the sum of the digits in the number 100!
"""

import math

if __name__ == "__main__":
  # Brute force!
  print sum(map(int, str(math.factorial(100))))
