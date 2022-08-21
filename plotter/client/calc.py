import math

def pyth(a, b, c):
  if a is None:
    return math.sqrt(c ** 2 - b ** 2)

  if b is None:
    return math.sqrt(c ** 2 - a ** 2)

  return math.sqrt(a ** 2 + b ** 2)
