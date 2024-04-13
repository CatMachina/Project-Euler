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
n = 3
start = 10 ** n - 1
end = 10 ** (n-1) - 1
for i in range(start, end, -1):
  for j in range(i, end, -1):
    if i * j == reverse(i * j):
      ans = max(ans, i * j)

print(ans)