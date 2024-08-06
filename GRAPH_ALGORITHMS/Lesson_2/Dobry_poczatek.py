# Dobry poczatek
# Wierzchołek v w grafie skierowanym nazywamy dobrym poczatkiem jesli
# kazdy inny wierzchołek mozna osiagnac sciezka skierowana wychodzaca z v. Prosze podac algorytm, który
# stwierdza czy dany graf zawiera dobry poczatek.

#użyjemy algorytmu Kosaraju's

from collections import deque

def DFS(G):
    visited = [False for i in range(len(G))]
    stack = deque()
    def DFS_visit(s):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                DFS_visit(v)
        stack.append(s)

    for v in range(len(G)):
        if not visited[v]:
            DFS_visit(v)

    return stack

#odwracanie grafu

def Graph_reverse(G):
    new_graph = [[] for _ in range(len(G))]

    for i in range(len(G)):
        for k in G[i]:
            new_graph[k].append(i)
    return new_graph
def SCC(G):

    stack = DFS(G)
    G = Graph_reverse(G)
    visited = [-1 for i in range(len(G))]
    token = 0


    def DFSu(v):
        visited[v] = token
        for u in G[v]:
            if visited[u] == -1:
                DFSu(u)

    while stack:
        v = stack.pop()
        if visited[v] == -1:
            DFSu(v)
            token += 1
    return visited


G = [[1],[2,3],[0],[4],[5],[3],[5,7],[8],[9],[6,10],[]]

print(SCC(G))

#łączenie SCC w jeden wierzchołek









#sortowanie Topologiczne


def SortingTopological(G):
    n = len(G)
    visited = [False] * n
    order = []

    def dfs(v):
       visited[v] = True
       for u in G[v]:
           if not visited[u]:
               dfs(u)
       order.append(v)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    order.reverse()

    return order
# puszczam DFSa z pierwszego vertexa po posortowaniu i sprawdzam czy odwiedził wszytkie vertexy jeśli tak to graf ma dobry początek
