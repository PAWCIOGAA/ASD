from math import inf
from egz2btesty import runtests
def maze(T):
    n = len(T)
    DP = [-1]*n
    DP[0] = 0
    for i in range(n):
        zloto_w_kieszeni = DP[i]
        zloto_w_szkrzyni = T[i][0]

        if DP[i] != -1:
            for j in range(1,4):
                cena_wejscia = T[i][j][0]
                nowa_komnata = T[i][j][1]
                if nowa_komnata > i and zloto_w_szkrzyni - cena_wejscia <= 10:
                    DP[nowa_komnata] = max(DP[nowa_komnata],min(zloto_w_szkrzyni -cena_wejscia,10)+zloto_w_kieszeni)

    return DP[n-1]


runtests( maze, all_tests = True )