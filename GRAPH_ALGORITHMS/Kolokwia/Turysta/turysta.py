from math import inf
from queue import PriorityQueue
from egzP1btesty import runtests
def Convert(L):
    maxi = max(max(u, v) for u, v, weight in L)
    G= [[] for _ in range(maxi+1)]

    for u,v,weight in L:
        G[u].append((v,weight))
        G[v].append((u, weight))
    return G


def Dijskra(G,start,end):
    n = len(G)
    weights = [[inf]*3 for _ in range(n)]
    weights[start][0] = 0
    weights[start][1] = 0
    weights[start][2] = 0
    pq = PriorityQueue()

    pq.put((0,3,start)) # weight,Pozostala ilosc,vertex
    while not pq.empty():
        waga, ilosc, vertex = pq.get()


        for v,weight in G[vertex]:
            if ilosc >0 and v != end:
                if weights[v][ilosc - 1] > waga + weight:
                    weights[v][ilosc - 1] = waga + weight
                    pq.put((weights[v][ilosc - 1],ilosc - 1,v))
            elif ilosc ==0 and v == end:
                weights[end][0] = min(weights[end][0],waga + weight)

    return weights[end][0]
def turysta3(G,D,L):
    G = Convert(G)
    return Dijskra(G,D,L)

runtests ( turysta3 )

