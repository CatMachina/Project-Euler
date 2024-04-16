# Perform the sequence on every possible number
# O(n * m), n = upper bound, m = longest chain ~500 in this case

def collatz(n):
  c = 0
  while n > 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    c += 1
  return c

n = 1000000
ans = 0
e = 0
for i in range(1, n):
  c = collatz(i)
  if c > ans:
    ans = c
    e = i
print(e, ans)

# Alternatively, can memoize certain values to prevent having to calculate the rest of the chain
# Don't really know a time complexity for this, but it's 10x faster than the previous solution for n = 1000000
dp = {}
def collatz_better(n):
  c = 0
  x = n
  while n > 1:
    if n in dp:
      dp[x] = c + dp[n]
      return dp[x]
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    c += 1
  dp[x] = c
  return dp[x]

ans = 0
e = 0
for i in range(1, n):
  c = collatz_better(i)
  if c > ans:
    ans = c
    e = i
print(e, ans)
