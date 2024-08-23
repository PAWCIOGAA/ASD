#F - zwraca minimalna ilosc operacji mnozenia macierzy
# n = dlugosc listy z macierzami   F(i,j) = for k in range(j):
#                                            left = F(i,k)
#                                            right = F(k+1,j)
#                                            return left*right    w uproszczeniu wszytko


def Mnozenie(A):
    n = len(A)

    DP = [[float('inf')]*n for _ in range(n)]

    for i in range(n):
        DP[i][i] = 0

    for i in range(n):
        DP[i][i+1] = A[i][0] * A[i][1] * A[i+1][1]


    for i in range(2,n):
        for j in range(n-i):
            for k in range(j,i+j):
                DP[j][j+i] = min(DP[j][j+i],DP[j][k] + DP[k+1][i+j] + A[j][0] * A[k][1] * A[i +j][1])
    return DP[0][n-1]



