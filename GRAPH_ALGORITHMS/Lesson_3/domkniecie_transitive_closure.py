from copy import deepcopy
def Floyd_Warshall(G):
    n = len(G)
    W = deepcopy(G)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not W[i][j]:
                    if W[i][k] and W[k][j]:
                        W[i][j] = True
    return W



