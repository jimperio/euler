"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

if __name__ == "__main__":
  sum_squares = sum(map(lambda i: i**2, range(1, 101)))
  square_sum = sum(range(1,101)) ** 2
  print square_sum - sum_squares
