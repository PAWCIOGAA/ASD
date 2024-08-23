

def Dynamic(A,k):
    n = len(A)
    DP = [[-1]*(k+1) for _ in range(n)]

    S = [0] * n
    S[0] = A[0]
    for i in range(1,n):
        S[i] = S[i-1]+ A[i]

    for i in range(n):
        DP[i][1] = S[i]


    for i in range(2,k+1):
        for j in range(i-1,n):
            for l in range(i-2,j):
                DP[j][i] = max(DP[j][i],min(DP[l][i-1],S[j] - S[i]))

    return DP[n][k+1]