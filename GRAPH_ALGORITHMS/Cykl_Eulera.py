def Euler_cycle(G):
    cykl  = []
    def DFS(v)

        while G[v]:
            u = G[v].pop()
            DFS(u)
        cykl.append(v)

    DFS(0)

    cykl = cykl.reverse()

    return cykl