"""
Dana jest mapa kraju w postaci grafu G = (V,E), gdzie wierzchołki to
miasta a krawedzie to drogi łaczace miasta. Dla kazdej drogi znana jest jej długosc (wyrazona w kilometrach
jako liczba naturalna). Alicja i Bob prowadza (na zmiane) autobus z miasta x > V do miasta y > V , zamieniajac
sie za kierownica w kazdym kolejnym miescie. Alicja wybiera trase oraz decyduje, kto prowadzi pierwszy.
Prosze zapropnowac algorytm, który wskazuje taka trase (oraz osobe, która ma prowadzic pierwsza), zeby
Alicja przejechała jak najmniej kilometrów.


Optymalizacja wysilku tylko jednego kierowcy

"""


from math import inf
from queue import PriorityQueue
def Dijskra(G,start,end,WhoStarts):
    n = len(G)
    weights = [inf for i in range(n)]
    parents = [None for i in range(n)]
    done = [False for i in range(n)]
    pq = PriorityQueue()
    pq.put( (0, start, WhoStarts) )
    weights[start] = 0

    while not pq.empty():
        _,u,name = pq.get()
        if done[u]: continue
        for v,weight in G[u]:
            if done[v]: continue
            if name == 'Alice':
                if weights[v] > weights[u] + weight:
                    weights[v] = weights[u] + weight
                    parents[v] = u
                    pq.put((weights[v],v,"Bob"))
            else:
                weights[v] = weights[u]
                parents[v] = u
                pq.put((weights[v], v,"Alice"))
        done[u] = True
        if u == end:
            return parents, weights[end]

    return parents

def Shortest_Path(G,a,b):
    o,p =  Dijskra(G,a,b,"Alice")
    c,d =  Dijskra(G,a,b,"Bob")
    if d < p:
        path = c
    else:path = d
    result = []
    result.append(b)
    while path[b] != None:
        result.append(path[b])
        b = path[b]

    result.reverse()

    return result,p,d


def createGWeight(edges, n):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b, weight = edge[0], edge[1], edge[2]
        G[a].append( (b, weight) )
        # G[b].append( (a, weight) )
    #
    return G

edges = [ (0, 3, 70), (0, 1, 100), (1, 2, 15), (1, 7, 33), (2, 8, 2), (2, 4, 15), (4, 5, 11), (5, 9, 1), (5, 6, 98), (9, 6, 47),
          (6, 10, 30), (7, 9, 63), (7, 8, 6), (0, 2, 54), (4, 8, 50), (3, 4, 20) ]

G = createGWeight(edges, 11)



print(Shortest_Path(G,0,10,))


print(Dijskra(G,0,10,"Alice"))

