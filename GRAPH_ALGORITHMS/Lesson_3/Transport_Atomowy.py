def Floyd_Warshall(G):
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]
    return G

from queue import Queue
def BFS(G,s):
    n = len(G)
    visited = [False] * n
    parents = [None] * n
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        if not visited[u]:
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    Q.put(v)
    return parents
from math import inf
def Transport_atomowy(G,d,s,t):
    n = len(G)
    Gr = [[G[i][j] for j in range(n)] for i in range(n)]
    G = Floyd_Warshall(G)
    new_Graph = [ [False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != inf and G[i][j] > d:
                new_Graph[i][j] = True

    Graph = [ [] for i in range(n * n)]

    for i in range(n):
        for j in range(n):
            if new_Graph[i][j]:
                for k in range(n):
                    if k != j and new_Graph[i][k] and Gr[j][k] != inf:
                        Graph[n*i + j].append(n*i + k)
                for k in range(n):
                    if k != i and new_Graph[k][j] and Gr[i][k] != inf:
                        Graph[n * i + j].append(n * k + j)
    parents = BFS(G,n*s +t)
    k = n*t + s
    path = []
    while k != None:
        path.append((k//n,k%n))
        k = path[k]
    path.reverse()
    if path[0] != (s,t): return False
    return True,path