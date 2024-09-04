
def DFS(G,ART,D,LOW,P,i):
    global time
    children = 0
    time += 1
    D[i] = time
    LOW[i] = time
    for s in G[i]:
        if D[s] is None:
            children += 1
            DFS(G,ART,D,LOW,s)
            if LOW[s] >= D[i]:
                ART[i] = True
            LOW[i] = min(LOW[s],LOW[i])

        else:
            LOW[i] = min(LOW[i],D[s])
    return children


def Articulation_Point(G):
    n = len(G)
    D = [None]*n        #discovery time
    LOW = [None]*n     # low
    P = [None]*n        #parent
    ART = [False]*n     # articulation point
    global time

    for i in range(n):
        if D[i] == None:
            if DFS(G, ART, D, LOW, P, i) > 1:
                ART[i] = True
            else:
                ART[i] = False

    return ART


