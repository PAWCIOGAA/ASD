
from collections import deque
def IndegreeCount(depends):
    n = len(depends)
    IndegreeArray = [0] * n

    for i in range(n):
        for j in depends[i]:
            IndegreeArray[i] += 1
    return IndegreeArray

def BFS(disk,depends):
    n = len(disk)
    IndegreeArray = IndegreeCount(depends)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    distans = [float('inf') for _ in range(n)]
    pq = deque()


    for i in range(n):
        if IndegreeArray[i] == 0:
            visited[i] = True
            distans[i] = 0
            pq.append(i)

    while pq:

        u = pq.popleft()

        if parents[u] != None:
            if disk[parents[u]] == disk[u]: distans[u] = distans[parents[u]]
            else:distans[u] = distans[parents[u]] + 1

        for v in depends[u]:
            IndegreeArray[v] -= 1
            if not visited[u] and IndegreeArray[v] <= 0:
                visited[v]  = True
                parents[v] = u
                if disk[v] == disk[u]: pq.appendleft(v)
                else: pq.append(v)

    return max(distans)



def swaps( disk, depends ):
    return BFS(disk,depends)


 # zmien all_tests na True zeby uruchomic wszystkie testy


