from queue import PriorityQueue
from math import inf
def prims(G):
    n = len(G)
    weights = [inf for i in range(n)]
    parent = [None for i in range(n)]
    done = [False for i in range(n)]
    pq = PriorityQueue()
    pq.put((0,0))

    while not pq.empty():
        e_weight,u = pq.get()
        if not done[u]:
            for v, weight in G[u]:
                if not done[v] and weights[v] > weight:
                    parent[v] = u
                    weights[v] = weight
                    pq.put((weights[v],v))
    return weights,parent