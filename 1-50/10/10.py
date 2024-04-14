# Use sieve of eratosthenes to compute the number of primes within a certain range quickly
# O(n log log n), n = upper bound, O(n) space

n = 2000000

sieve = [True] * n
sum = 0
for i in range(2, n):
  if sieve[i]:
    sum += i
    for j in range(i + i, n, i):
      sieve[j] = False

print(sum)
