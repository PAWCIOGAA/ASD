from math import inf
from egz2atesty import runtests

def coal(A,T):
    n = len(A)
    DP = [T]*n
    last_conteiner = inf
    for i in range(n):
        for j in range(i+1):
            if DP[j] - A[i] >=0:
                DP[j] = DP[j] - A[i]
                last_conteiner = j
                break

    return last_conteiner


runtests( coal, all_tests = True )