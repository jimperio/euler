"""
Starting in the top left corner of a 2x2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

from math import factorial

def get_num_routes(w, h):
  # This is equivalent to finding the number of permutations of a set with
  # w elements of one kind and h elements of another, i.e., w rights and h downs.
  return factorial(w + h) / (factorial(w) * factorial(h))

if __name__ == "__main__":
  print get_num_routes(20, 20)
