from queue import PriorityQueue
from math import inf
def Dijskra(G,s):
    n = len(G)
    parents = [None for i in range(n)]
    weights = [inf for i in range(n)]
    pq = PriorityQueue()
    pq.put((0,s))

    while not pq.empty():
        _,u = pq.get()
        for v,weight in G[u]:
            if weights[v] > weights[u] + weight:
                weights[v] = weights[u] + weight
                parents[v] = u
                pq.put((weights[v],v))
    return parents, weights