# Just iterate through all the terms and add the even-valued ones
# Fibonnaci numbers increase at an exponential rate (with base of golden ratio)
# O(log n) where n = upper bound
a = 1
b = 2
sum = 2
upper = 4000000
while a + b < upper:
  c = a + b
  if c % 2 == 0:
    sum += c
  a = b
  b = c

print(sum)