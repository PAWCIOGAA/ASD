from math import inf
from queue import  PriorityQueue
from jumpertesty import runtests

def FromMatrixTo(M):
    n = len(M)
    G = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
          if M[i][j] > 0:
            G[i].append((j,M[i][j]))
            G[j].append((i,M[i][j]))
    return G

def Dijskra(G,s,w):
    n = len(G)
    weights = [[inf] *2 for i in range(n)] # first columnt without shoes, second with shoes
    weights[s][0] = 0
    weights[s][1] = 0
    pq = PriorityQueue()
    pq.put((0,False,s)) # weight,czy buty, wierzchołek

    while not pq.empty():
        waga, buty, u = pq.get()

        if u == w: return waga

        for v,weight in G[u]:
            if weights[v][0] > waga + weight:
                weights[v][0] = waga + weight
                pq.put((weights[v][0],False,v))

            if buty == False:
                for v_1, weight_1 in G[v]:
                    if weights[v_1][1] > max(waga + weight_1,waga + weight):
                        weights[v_1][1] = max(waga + weight_1,waga + weight)
                        pq.put((weights[v_1][1],True,v_1))

def jumper(G,s,w):
    G = FromMatrixTo(G)
    return Dijskra(G,s,w)

runtests(jumper)