def Plecak(T,W,H):
    n = len(T)
    # T[cena,waga,wyskośc]
    DP = [[ [0]*(H+1) for _ in range(W+1)] for _ in range(n)]

    for i in range(n):
        DP[i][0][0] = 0

    for i in range(W+1):
        for j in range(H+1):
            if T[0][1] <= i and T[0][2] <= j:
                DP[0][i][j] = T[0][0]


    for i in range(1,n):
        for j in range(1,W+1):
            for k in range(1,H+1):
                if T[i][1] <= j and T[i][2] <= k:
                    DP[i][j][k] = max(DP[i-1][j][k],T[i][0] + DP[i-1][j - T[i][1]][k - T[i][2]])
                else: DP[i][j][k] = DP[i-1][j][k]

    return DP[n-1][W][H]

