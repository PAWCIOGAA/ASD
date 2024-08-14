"""
Dany jest graf G = (V,E), gdzie kazda krawedz ma wage
ze zbioru {1, . . . , SES} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych
wierzchołków x i y oblicza sciezke o najmniejszej sumie wag, która prowadzi z x do y po krawedziach o
malejacych wagach (jesli sciezki nie ma to zwracamy ª).
"""

from queue import PriorityQueue
from math import inf

def Dijskra(G,a,b):
    n = len(G)
    done = [False for _ in range(n)]
    weights = [inf for _ in range(n)]
    parents = [None for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0,inf,a))
    weights[a] = 0

    while not pq.empty():
        _, lastWeight, u = pq.get()
        if not done[u]:
            for v,weight in G[u]:
                if weight < lastWeight and not done[v] and weights[v] > weights[u] + weight:
                    weights[v] = weights[u] + weight
                    pq.put((weights[v],weight,v))
                    parents[v] = u
        if u == b:
            return parents

    return None


def path(G,a,b):
    path = Dijskra(G,a,b)

    result = []
    result.append(b)
    while path[b] != None:
        result.append(path[b])
        b = path[b]
    result.reverse()
    return result

G = [[(1,10),(4,20)],[(0,10),(2,9)],[(3,8),(1,9)],[(2,11),(6,17)],[(0,20),(5,19)],[(4,19),(6,18)],[(5,18),(3,17)]]

print(path(G,0,3))