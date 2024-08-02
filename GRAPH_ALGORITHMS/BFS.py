from queue import Queue
def BFS(G:'graf',s:'wierzchołek startowy'):
    visited = [False] * len(G)
    parents = [None] * len(G)
    Q = Queue()
    visited.s = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if visited[v] != True:
                visited[v] = True
                parents[v] = u
                Q.put(v)

    return visited, parents