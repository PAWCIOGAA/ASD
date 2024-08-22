# F zzwraca długość najdłższego podciągu do n rekurencyjna
# F(n,n) = max(F(n-1,n),F(n,n-1))

def Najdluzszy(A,B):
    n = len(A)
    m = len(B)
    DP = [[0]*n for _ in range(m)]

    for i in range(n):
        if B[0] == A[i]:
            DP[0][i] = 1
    for i in range(m):
        if A[0] == B[i]:
            DP[i][0] = 1

    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j],DP[i][j-1])

    return DP[n-1][j-1]