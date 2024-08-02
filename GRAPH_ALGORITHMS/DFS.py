def DFS(G,u):
    visited = [False] * len(G)
    parents = [None] * len(G)

    def DFS_VISIT(G,s):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                parents[v] = s
                DFS_VISIT(G,v)
    DFS_VISIT(G,u)
    return visited, parents

