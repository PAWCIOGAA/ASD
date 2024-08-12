from queue import PriorityQueue
from math import inf
def Dijskra(G,s):
    n = len(G)
    parents = [None for i in range(n)]
    weights = [inf for i in range(n)]
    done = [False for i in range(n)]
    pq = PriorityQueue()
    pq.put((0,s))
    weights[s] = 0

    while not pq.empty():
        _,u = pq.get()
        if not done[u]:
            for v,weight in G[u]:
                if weights[v] > weights[u] + weight and not done[v]:
                    weights[v] = weights[u] + weight
                    parents[v] = u
                    pq.put((weights[v],v))
            done[u] = True
    return parents, weights