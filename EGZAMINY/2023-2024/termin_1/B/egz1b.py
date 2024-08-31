from egz1btesty import runtests
from math import inf

def kstrong( T, k):
  # tu prosze wpisac wlasna implementacje
  n = len(T)
  DP = [[-inf]*(k+1) for _ in range(n)]
  max_sum = T[0]
  for j in range(k+1):
    DP[0][j] = T[0]

  for i in range(n):
    for j in range(k+1):

      DP[i][j] = max(DP[i][j],DP[i-1][j] + T[i],T[i])
      if j > 0:
        DP[i][j] = max(DP[i][j], DP[i - 1][j - 1])

      max_sum = max(max_sum, DP[i][j])

  return max_sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = False )
