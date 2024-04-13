# Can just loop through 100 numbers fairly quickly and calculate both values iteratively
# O(n), n = upper bound

n = 100
sum_t = 0
sum_s = 0
for i in range(n+1):
  sum_t += i
  sum_s += i ** 2
sum_t **= 2
print(sum_t - sum_s)

# Alternatively, can use formulas for sum of natural numbers (triangle numbers) and sum of squares of natural numbers (a.k.a square pyramidal numbers)
# O(1)
triangle = lambda x: x * (x+1) // 2
spn = lambda x: (2 * x + 1) * (x + 1) * x // 6

print(triangle(n) ** 2 - spn(n))