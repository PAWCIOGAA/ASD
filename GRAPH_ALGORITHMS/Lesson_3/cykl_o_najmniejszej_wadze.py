#graf skierowany

#pomysł 2 na przekątnej ustwiam inf i wykonuje Floyda-Warshalla a następnie szukam minimum na przekątnej

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
    return W


def MinCycle(G):
    n = len(G)
    answer = float('inf')
    distance = Floyd_Warshall(G)

    for i in range(n):
        for j in range(n):
            if i != j:
                answer = min(answer,distance[i][j] + distance[j][i])
    return answer


#graf nieskierowany
from math import inf
from queue import PriorityQueue
def Dijskra(G:'matrix',a,b):
    n = len(G)
    done = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    distance[a] = 0
    pq = PriorityQueue()
    pq.put((0,a))

    while not pq.empty():
        _,u = pq.get()
        if not done[u]:
            for v in range(n):
                if done[v]: continue
                if G[u][v] != -1 and distance[v] > distance[u] + G[u][v]:
                    distance[v] = distance[u] + G[u][v]
                    pq.put((distance[v],v))
            done[u] = True
            if u == b: return distance[b]



    return distance

def MinCycle_undirected(G):
    n = len(G)
    result = inf
    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                weight = G[i][j]
                G[i][j] = -1
                result = min(Dijskra(G,i,j)+ weight,result)
                G[i][j] = weight

    return result

