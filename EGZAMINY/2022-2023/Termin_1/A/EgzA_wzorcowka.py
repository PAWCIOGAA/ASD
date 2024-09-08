from math import inf
from queue import PriorityQueue
from egz1Atesty import runtests

def Dijskra(G,s):
    n = len(G)
    weights = [inf for _ in range(n)]
    done = [False for _ in range(n)]
    PQ = PriorityQueue()
    PQ.put((0,s))
    weights[s] = 0

    while not PQ.empty():
        time, vertex = PQ.get()
        if not done[vertex]:
            for v , weight in G[vertex]:
                if not done[v]:
                    if weights[v] > time + weight:
                        weights[v] = time + weight
                        PQ.put((weights[v],v))
            done[vertex] = True
    return weights


def gold(G,V,s,t,r):
    n = len(G)
    koszt_przed = Dijskra(G,s)

    #modyfikuje graf
    for v in range(n):
        for e in range(len(G[v])):
            now_tupla = (G[v][e][0],(G[v][e][1] * 2) + r)
            G[v][e] = now_tupla

    koszt_po = Dijskra(G,t)

    min_koszt = koszt_przed[t]
    for v in range(n):
        ile_zarobowal = V[v]
        koszt_przejscia = koszt_przed[v] + koszt_po[v] - ile_zarobowal
        min_koszt = min(min_koszt,koszt_przejscia)

    return min_koszt

runtests( gold, all_tests = True )
