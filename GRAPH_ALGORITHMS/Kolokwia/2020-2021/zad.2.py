# czy po usunięciu jakiejś krawędzi z najkrótszej ścieżki ona się zmieni???

from queue import Queue
def BFS(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    parents = [None for _ in range(n)]
    Q = Queue()
    Q.put(s)
    visited[s] = True
    distance[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                distance[v] = distance[u] + 1
                visited[v] = True
                Q.put(v)
    return distance,parents

def enlarge(G,s,t):
    distance, parents = BFS(G,s)
    if distance[t] == float('inf'): return
    wynik = distance[t]
    sciezka = []

    while parents[t] != None:
        sciezka.append(t)
        t = parents[t]

    for krawedz in sciezka:
        G[krawedz[0]].remove(krawedz[1])
        G[krawedz[1]].remove(krawedz[0])

        distance, parents = BFS(G,s)
        if distance[t] > wynik: return krawedz

        G[krawedz[0]].append(krawedz[1])
        G[krawedz[1]].append(krawedz[0])

    return None





