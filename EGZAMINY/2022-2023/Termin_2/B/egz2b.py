from math import inf
from egz2btesty import runtests
def parking(X,Y):
    n = len(X)
    m = len(Y)

    DP = [[inf]*m for _ in range(n)]

    for i in range(m):
        DP[0][i] = abs(Y[i] - X[0])


    for i in range(1,n):
        mini = DP[i-1][i-1]
        for j in range(i,m):
            mini = min(mini,DP[i-1][j-1])
            DP[i][j] = mini + abs(X[i] - Y[j])

    return min(DP[n-1])

runtests( parking, all_tests = True)