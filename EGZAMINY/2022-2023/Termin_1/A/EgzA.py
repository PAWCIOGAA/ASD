from math import inf
from queue import PriorityQueue
from egz1Atesty import runtests


def gold(G,V,s,t,r):
    n = len(G)

    weights = [[inf]*(n+1) for _ in range(n)]
    for i in range(n):
        weights[s][i] = 0
    weights[s][1] = V[s]
    PQ = PriorityQueue()
    PQ.put((0,s,-1))  # weight, vertex, if some castle already robbed
    PQ.put((-30,s,1))

    while not PQ.empty():
        gold , vertex , IFrobbed = PQ.get()

        for v , weight in G[vertex]:
            # nie obrabiam banku
            if  IFrobbed == -1:
                if weights[v][0] > gold + weight:
                    weights[v][0] = gold + weight
                    PQ.put((weights[v][0],v,-1))
                #obrabiam bank
                if weights[v][v+1] > gold + weight - V[v]:
                    weights[v][v + 1] = gold + weight - V[v]
                    PQ.put((weights[v][v+1],v,v+1))

            #jakiś zamek był już obrabowany
            else:
                if weights[v][IFrobbed] > gold + weight*2 + r:
                    weights[v][IFrobbed] = gold + weight * 2 + r
                    PQ.put((weights[v][IFrobbed], v,IFrobbed))

    return min(weights[t])


runtests( gold, all_tests = True )




