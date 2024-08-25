def zaba(A):
    n = len(A)
    DP = [[float('inf')]*n for _ in range(n)]
    # rows is energy, columns ar filds indexes

    DP[0][0] = 0

    for i in range(n):
        DP[i][0] = 0

    for i in range(A[0]):
        DP[i][A[0]-i] = 1

    for i in range(n):
        for j in range(n):
            if DP[i][j] != float('inf'):
                for k in range(i):
                    new_energy = min(A[j] + i, n-1 - j)

                    for k in range(new_energy):
                        DP[k][j + new_energy - k] = min(DP[k][j + new_energy - k],DP[i][j] + 1)

    return DP[0][n-1]