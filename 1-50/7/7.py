# Keep track of list of primes and use to determine if other numbers are prime
# According to Prime Number Theorem (PNT), # of primes <= n ~ n / log(n)
# Each iteration of checking can thus approximated as sqrt(x) / log (x) for iteration x, or total
# O(n * sqrt(n) / log (n)), n = n-th prime needed
# Alternatively, sieve methods can be used (e.g. sieve of eratosthenes), but an upper bound needs to be known beforehand
# This can be calculated however, there are solutions in the forum that tackle this!

n = 10001
primes = []
i = 2
while len(primes) < n:
  is_prime = True
  for p in primes:
    if p * p > i:
      break
    if i % p == 0:
      is_prime = False
      break
  if is_prime:
    primes.append(i)
  i += 1

print(primes[-1])