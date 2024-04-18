

ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
def score(n):
  sum = 0
  if n >= 100:
    sum += 7
    sum += ones[n // 100]
    if n % 100 > 0:
      sum += 3
  n %= 100
  if n >= 20:
    sum += tens[n // 10]
  elif n >= 10:
    sum += teens[n - 10]
    n = 0
  n %= 10
  sum += ones[n]
  return sum

n = 1000
sum = 0
for i in range(1, n):
  # print(i, score(i))
  sum += score(i)
sum += 11
print(sum)