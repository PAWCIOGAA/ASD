def DFS(G,u):
    visited = [False] * len(G)
    order = []
    def DFS_Visit(G,s):
        visited[s] = True

        for v in G[s]:
            if not visited[v]:
                DFS_Visit(G,v)
        order.append(G[s])
    DFS_Visit(G,u)

    for k in range(len(G)):
        if not visited[k]:
            DFS_Visit(G,k)
    order.reverse()
    return order


B = [[],[0,2,3],[0],[2,0]]


def Hamilton(G:'adjency list'):
    path = DFS(G,0)
    n = len(G)
    for i in range(n-1):
        a = path[i]
        b = path[i+1]
        if b not in G[a]:
            return False

    return True