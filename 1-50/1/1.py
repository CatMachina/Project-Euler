# Just count all multiples of either by iterating to upper bound
# O(n)
sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)

# Alternatively, use triangle numbers to count sum and inclusion/exclusion principle to prevent double counting
# O(1)
upper = 999
triangle = lambda x: x * (x + 1) // 2
three = triangle(upper // 3)
five = triangle(upper // 5)
fifteen = triangle(upper // 15)
ans = three * 3 + five * 5 - 15 * fifteen
print(ans)
