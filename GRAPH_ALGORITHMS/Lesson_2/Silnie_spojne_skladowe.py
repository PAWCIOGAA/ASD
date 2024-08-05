def DFS(G,s):
    visited = [False] * len(G)
    times = [0] * len(G)
    time = 0
    def DFS_visit(G,s):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                DFS(G,v)
        nonlocal time
        time += 1
        times[s] = time

    for k in range(len(G)):
        if not visited[k]:
            DFS_visit(G,k)



    return times

def Transpose_graph(G:'adjency list'):
    new_graph = [[] for _ in range(len(G))]

    for i in range(len(G)):
        for k in range(len(G[i])):
            new_graph[k].append(i)

    return new_graph

def Order(times):

    n = len(times)
    order = [0 for i in range(n)]
    for i in range(n):
        order[n - times[i]] = i
    return order

def Znajdowalnie_silnych_skladowych(G):
    n = len(G)
    times = DFS(G,0)
    graph = Transpose_graph(G)
    order = Order(times)
    result = [-1] * len(G)
    token = 0
    def dfsu(u):
        result[u] = token
        for v in G[u]:
            if result[v]<0:
                dfsu(v)

    for i in range(n):
        u = order[i]
        if result[u] < 0:
            dfsu(u)
            token += 1
    return result