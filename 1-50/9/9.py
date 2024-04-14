# Iterate through possible pairs (a, b)
# Equation only has 2 dof, since c = 1000 - a - b, so
# O(n^2)

n = 1000
for a in range(1, n):
  for b in range(a, n):
    c = 1000 - a - b
    if a < b and b < c and a ** 2 + b ** 2 == c ** 2:
      print(a * b * c)

# Alternatively, math can be done by finding base triplets that add up to a divisor of 1000, then multiply the triplet by whatever factor you need
# Have to find pythagoreon triplet (8, 15, 17), since 8+15+17=40, then multiply by 1000/40=25