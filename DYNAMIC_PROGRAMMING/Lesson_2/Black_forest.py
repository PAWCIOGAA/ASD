def Black_forest(T):
    n = len(T)
    m = int(n//2 + 1.5)
    DP = [[0]*m for _ in range(n)]

    for i in range(1,m):
        DP[0][i] = T[0]

    max_two_trees = max(T[0],T[1])

    for i in range(1,m):
        DP[1][i] = max_two_trees


    for i in range(2,n):
        for j in range(1,m):
            DP[i][j] = max(DP[i-2][j-1] + T[i],DP[i-1][j])

    return DP[n-1][n-1]

