# Realize that # of paths follows Pascal's triangle, so add previous row/column
# O(n^2), n = side length of matrix
n = 20
n += 1
dp = [[0] * n for i in range(n)]
dp[0][0] = 1
for i in range(0, n):
  for j in range(0, n):
    if i > 0:
      dp[i][j] += dp[i-1][j]
    if j > 0:
      dp[i][j] += dp[i][j-1]
print(dp[-1][-1])


# Alternatively, realize again that each entry of Pascal's triangle is equal to an n choose k formula
# Or, realize that n rights and n downs must occur but in any order and same directions are non-distinct
# => use permutation without distinction with certain amount of each element => (2n!)/(n!)^2
# O(n), if you consider all operations O(1), constant space
ans = 1
for i in range(40, 20, -1):
  ans *= i / (i-20)
print(int(ans))