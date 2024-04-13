# Palindrome number = reverse is same as forward
# Brute force check all numbers for largest palindrome
# O(10^(2n)), n = # of digits of divisors given

def reverse(n):
  x = 0
  while n > 0:
    x = x * 10 + n % 10
    n //= 10
  return x

ans = 0
for i in range(999, 99, -1):
  for j in range(999, 99, -1):
    if i * j == reverse(i * j):
      ans = max(ans, i * j)

print(ans)