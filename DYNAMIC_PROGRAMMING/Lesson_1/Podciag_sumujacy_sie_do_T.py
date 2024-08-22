#czy istnieje podciąg ciągu liczb naturalnych, który sumuje się do T

# F rekurencyjna   F(A,T,n) = F(A,T-A[n],n-1) or F(A,T,n-1)

def Podciag_do_T(A,T):

    DP = [[False for _ in range(T+1)] for _ in range(len(A) + 1)]
    for i in range(len(A) + 1):
        DP[i][0] = True

    for i in range(1,len(A)):
        for j in range(1,T+1):
            if A[i-1] > j:
                DP[i][j] = DP[i - 1][j]
            else:
                DP[i][j] = DP[i-1][j] or DP[i-1][j - A[i-1]]

    return DP[len(A)][T]

