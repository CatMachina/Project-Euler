# Factorize the number, by iterating from smallest to highest, small prime factors are factorized first
# Continuing means that larger prime factors MUST exist
# O(sqrt(n)), n = given number
n = 600851475143

i = 2
ans = 1
while i * i <= n:
  if n % i == 0:
    n = n // i
    ans = i
    print(i)
  else:
    i += 1
print(n)
print(ans)