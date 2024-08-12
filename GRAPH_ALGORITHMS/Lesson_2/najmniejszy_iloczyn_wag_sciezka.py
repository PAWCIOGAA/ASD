from math import inf,log10
from queue import PriorityQueue
def Dijskra(G,start,end):
    n = len(G)
    weights = [inf for i in range(n)]
    parents = [None for i in range(n)]
    done = [False for i in range(n)]

    pq= PriorityQueue()
    pq.put((0,start))
    weights[start] = 0

    while not pq.empty():
        _,u = pq.get()
        if not done[u]:
            for v,weight in G[u]:
                if not done[v] and relax(weights,parents,u,v,weight):
                    pq.put((weights[v],v))
            done[u] = True

        if done[end]:
            return parents




def relax(weights,parents,u,v,weight):
    if weights[v] > weights[u] + log10(weight):
        weights[v] = weights[u] + log10(weight)
        parents[v] = u
        return True
    return False

def Shortest_Path(G,a,b):
    path = Dijskra(G,a,b)
    result = []
    result.append(b)
    while path[b] != None:
        result.append(path[b])
        b = path[b]

    result.reverse()

    return result

graph = [[(1, 20), (2, 30)],
         [(0, 20), (3, 12), (4, 11)],
         [(0, 30), (3, 18), (5, 2700)],
         [(1, 12), (2, 18), (8, 22), ],
         [(1, 11), (6, 15)],
         [(2, 2700), (7, 19), (8, 3)],
         [(4, 15), (8, 8)],
         [(5, 19)],
         [(3, 22), (5, 3), (6, 8)]]

u, v = 0, 7

print(Shortest_Path(graph,u,v))