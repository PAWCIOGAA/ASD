from copy import deepcopy
def Floyd_Warshall(G:'matrix'):
    W = deepcopy(G)
    n = len(G)

    path = [[None for _ in range(n)] for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][j] > W[i][k] + W[k][j]:
                    W[i][j] = W[i][k] + W[k][j]
                    path[i][j] = k

    #Sprawdzam czy istnieje ujemny cykl poprzez sprawdzenie przekątnej macierzy(jeśli coś jest <0 to oznacza że jest ujemny cykl)


    for i in range(n):
        if W[i][i] <0: return "Mamy ujemny cykl :("

    return W