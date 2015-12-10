"""
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def fibs(limit):
  xs = [1, 2]
  while True:
    xs.append(xs[-2] + xs[-1])
    if xs[-1] > limit:
      break
  while xs[-1] > limit:
    xs.pop(-1)
  return xs

if __name__ == "__main__":
  print sum(filter(lambda i: i % 2 == 0, fibs(4000000)))
