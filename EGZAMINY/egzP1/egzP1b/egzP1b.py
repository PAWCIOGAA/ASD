from egzP1btesty import runtests 

def Graph_convert(M):
    maxi = max(max(u,v) for u,v,weight in M)
    G = [[] for _ in range(maxi+1)]
    for u,v, weight in M:
        G[u].append((v,weight))
        G[v].append((u,weight))
    return G


from queue import  PriorityQueue
from math import inf
def Dijsktra(G,s,end):
    n = len(G)
    weights = [[inf]*3 for _ in range(n)]
    PQ = PriorityQueue()
    weights[s][0] = 0
    weights[s][1] = 0
    weights[s][2] = 0

    PQ.put((0,3,s)) # time, vertices left to visit, vertex

    while not PQ.empty():
        time, left_vertices, vertex = PQ.get()

        for v ,weight in G[vertex]:
            if left_vertices  > 0 and v != end:
                if weights[v][left_vertices-1] > time + weight:
                    weights[v][left_vertices - 1] = time + weight
                    PQ.put((weights[v][left_vertices - 1],left_vertices-1,v))
            elif left_vertices == 0 and v == end:
                weights[end][0] = min(weights[end][0],time + weight)

    return weights[end][0]


def turysta( G, D, L ):
    G = Graph_convert(G)
    return Dijsktra(G,D,L)
    #tutaj proszę wpisać własną implementację

runtests ( turysta )