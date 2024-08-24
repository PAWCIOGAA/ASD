def Szachownica(T):
    n = len(T)
    DP = [[float('inf')]*n for _ in range(n)]

    DP[0][0] = T[0][0]
    for i in range(1,n):
        DP[i][0] = DP[i-1][0] + T[i][0]
        DP[0][i] = DP[0][i-1] + T[0][i]


    for i in range(1,n):
        for j in range(1,n):
            DP[i][j] = min(DP[i-1][j] + T[i][j],DP[i][j-1]+T[i][j])

    return DP[n-1][n-1]