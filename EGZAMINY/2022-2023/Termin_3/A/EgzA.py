from math import inf
from queue import PriorityQueue
from egz3atesty import runtests
def goodknight(G,s,t):
    n = len(G)
    weights = [[inf]*(16+1) for _ in range(n)]
    weights[s][0] = 0
    PQ = PriorityQueue()
    PQ.put((0,s,0)) # Complete time, vertex,time of walking

    while not PQ.empty():
        time, vertex,RoadTime = PQ.get()

        for i in range(n):
            if G[vertex][i] != -1:
                if RoadTime + G[vertex][i] <= 16:
                    if weights[i][RoadTime] > time + G[vertex][i]:
                        weights[i][RoadTime] = time + G[vertex][i]
                        PQ.put((weights[i][RoadTime],i,RoadTime + G[vertex][i]))
                else:
                    if weights[i][G[vertex][i]] > time + G[vertex][i] + 8:
                        weights[i][G[vertex][i]] = time + G[vertex][i] + 8
                        PQ.put((weights[i][G[vertex][i]],i,G[vertex][i]))

    return min(weights[t])



runtests( goodknight, all_tests = True )