"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def gen_fibs():
  a = 1
  b = 1
  yield a
  while True:
    c = b
    b += a
    a = c
    yield a


if __name__ == "__main__":
  index = 0
  for i in gen_fibs():
    index += 1
    if len(str(i)) == 1000:
      print index
      break
