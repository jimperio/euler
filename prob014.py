"""
The following iterative sequence is defined for the set of positive integers:

  n -> n/2 (n is even)
  n -> 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
"""

def get_longest_collatz_start_under(limit):
  max_count = 0
  max_start = 0
  for start in range(1, limit):
    count = sum(1 for i in gen_collatz(start))
    if count > max_count:
      max_count = count
      max_start = start
  return max_start


def gen_collatz(num):
  while num > 1:
    num = next_collatz(num)
    yield num

def next_collatz(n):
  if n % 2 == 0:
    return n / 2
  else:
    return 3 * n + 1

if __name__ == "__main__":
  # 38s on my MBP. Could be better!
  print get_longest_collatz_start_under(1000000)
