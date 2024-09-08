from math import inf
from egz1btesty import runtests
def planets(D,C,T,E):
    n = len(D)
    DP = [[inf]*(E+1) for _ in range(n)]

    for i in range(E+1):
        DP[0][i] = i * C[0]
    DP[T[0][0]][0] = min(DP[T[0][0]][0],DP[0][0] + T[0][1])


    for i in range(1,n):
        fuel_cost = C[i]
        distance = D[i] - D[i-1]

        for fuel in range(E+1):
            if fuel + distance <= E:
                DP[i][fuel] = min(DP[i][fuel],DP[i-1][fuel+ distance] )
        for fuel in range(1,E+1):
            DP[i][fuel] = min(DP[i][fuel],DP[i][fuel-1] + fuel_cost)

        dest,cost = T[i]
        DP[dest][0] = min(DP[dest][0],DP[i][0] + cost)
    return min(DP[n-1])
runtests( planets, all_tests = True )