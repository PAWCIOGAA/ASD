from math import inf
def BellmanFord(G,source):
    n = len(G)
    distance = [inf for _ in range(n)]
    distance[source] = 0
    parents = [None for _ in range(n)]

    for _ in range(n-1):
        for i in range(n):
            for j,weight in G[i]:
                if distance[j] > distance[i] + weight and distance[i] != inf:
                    distance[j] = distance[i] + weight
                    parents[j] = i

#checking if there is no negative cycle
    for i in range(n):
        for j, weight in G[i]:
            if distance[j] > distance[i] + weight:
                return "Negative cycle"


    return distance, parents
