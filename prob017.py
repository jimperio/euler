"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

import math

def count_letters_of_numbers_up_to(limit):
  return sum(map(lambda w: len(w), (to_words(n) for n in xrange(1, limit+1))))

words = {
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety'
}

units = {
  100: 'hundred',
  1000: 'thousand'
}

def to_words(number):
  # Works up to 9999.
  if number in words:
    return words[number]
  # NOTE: math.log(1000, 10) = 2.9999999999999996!
  # Use math.log10 instead.
  n = int(math.floor(math.log10(number)))
  unit = 10 ** n
  first_digit = (number / unit) % 10
  rest = number % (unit)
  if n == 1:
    # Handle numbers 20-99.
    return words[10 * first_digit] + to_words(rest)
  result = words[first_digit]
  if unit in units:
    result += units[unit]
    # Add the 'and' if needed.
    if rest > 0 and unit == 100:
      result += 'and'
  if rest > 0:
    result += to_words(rest)
  return result


if __name__ == "__main__":
  print count_letters_of_numbers_up_to(1000)
