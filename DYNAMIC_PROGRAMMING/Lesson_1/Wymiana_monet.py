def Money_change(A:'tablica monet',T:'kwota'):
    n = len(A)
    DP = [[float('inf')]*(T+1) for _ in range(n+1)]

    for i in range(n):
        DP[0][i] = 0

    for i in range(1,T+1):
        for j in range(1,n):
            if j <= A[i-1]:
                DP[i][j] = min(DP[i-1][j],DP[i][j - A[i-1]])
            else: DP[i][j] = DP[i-1][j]

    return DP[n][T]
