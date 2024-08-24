
def MiesciSie(A,C):
    a,b = A
    a1,b1 = C

    if a1>= a and b1 <= b:
        return True
    return False


def Klocki(T):
    n = len(T)
    DP = [[0]*n for _ in range(n)]

    for i in range(n):
        DP[0][i] = 1
        DP[i][0] = 1
        if MiesciSie(T[0],T[1]):
            DP[1][i] = 2
        else:DP[1][i] = 1


    for i in range(1,n):
        for j in range(1,n):
            for k in range(i):
                DP[i][j] = max(DP[i][j-1],DP[i-1][j])
                if MiesciSie(T[i],T[k]):
                    DP[i][j] = max(DP[i][j],DP[k][j-1])
    return n - DP[n-1][n-1]


#-----------------------------------------------------------
# drugie rozwiązanie lepsze

def klocki(T):
    n = len(T)
    DP = [1]*n

    for i in range(n):
        DP[i] = DP[i - 1]
        for j in range(i):
            if MiesciSie(T[j],T[i]):
                DP[i] = max(DP[i],DP[j] + 1)

    return n - DP[n-1]
