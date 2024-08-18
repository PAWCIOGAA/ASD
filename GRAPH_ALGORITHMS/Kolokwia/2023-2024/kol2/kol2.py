from typing import List, Any

from kol2testy import runtests
from queue import PriorityQueue
from math import inf

def Convert(M):
  max_vertex = max(max(u, v) for u, v, weight in M)
  n = max_vertex + 1

  # Initialize an empty adjacency list for each vertex
  G = [[] for _ in range(n)]

  for u ,v , weight in M:
    G[u].append((v, weight))
    G[v].append((u, weight))
  return G



def Dijskra(G,s,t):
  n = len(G)
  weights= [[inf] * 17 for i in range(n)]
  pq = PriorityQueue()
  weights[s][0] = 0
  pq.put((0,0,s))

  while not pq.empty():
    Total_time, Resting_time, vertex = pq.get()

    if vertex == t: return Total_time

    for v ,weight in G[vertex]:
      new_time = Resting_time + weight

      if new_time <= 16:
        if weights[v][new_time] > Total_time + weight:
          weights[v][new_time] = Total_time + weight
          pq.put((weights[v][new_time],new_time,v))
      else:
        new_resting_time = Total_time + weight + 8
        if weights[v][weight] > new_resting_time:
          weights[v][weight] = new_resting_time
          pq.put((new_resting_time,weight,v))
  return inf


def warrior( G, s, t):
  # tu prosze wpisac wlasna implementacje
  M = Convert(G)
  result = Dijskra(M,s,t)

  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
