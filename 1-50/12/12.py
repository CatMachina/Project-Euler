# Iterate through all triangle numbers, since the number of divisors doesn't scale exactly linearly
# Can compute triangle numbers in O(1) through a formula
# Count divisors with trial division up to sqrt triangle number
# O(n^2), n = the answer is the nth triangle number

triangle = lambda x: x * (x+1) // 2
i = 1
while True:
  n = triangle(i)
  j = 1
  c = 0
  while j * j <= n:
    if n % j == 0:
      c += 1 if n / j == j else 2
    j += 1
  if c >= 500:
    print(i, n)
    break
  i += 1