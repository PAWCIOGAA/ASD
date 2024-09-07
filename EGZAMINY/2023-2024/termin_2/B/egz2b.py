from egz2btesty import runtests
from collections import deque
from math import inf

def Convert(M):
  maxi = max(max(u,v) for u,v,weight,rail_type in M)
  G = [[] for _ in range(maxi+1)]

  for u,v,weight,rail_type in M:
    G[u].append((v,weight,int(rail_type == 'I')))
    G[v].append((u,weight,int(rail_type == 'I')))

  return G
def tory_amos( E, A, B ):
  # tu prosze wpisac wlasna implementacje
  G = Convert(E)
  n = len(G)
  Q = deque()
  weights = [[inf]*2 for _ in range(n)]
  weights[A][0] = -10
  weights[A][1] = -5

  Q.append((-10,A,0,0))
  Q.append((-5, A, 0, 1))

  while Q:
    weight,vertex,ping,rail_type = Q.popleft()

    if ping > 0:
      Q.append((weight,vertex,ping-1,rail_type))
      continue

    if weight == weights[vertex][rail_type]:
      for u,time,type in G[vertex]:
        if rail_type == type:
          if type == 0:
            if weights[u][0] > weight + time + 10:
              weights[u][0] = weight + time + 10
              Q.append((weights[u][0],u,time,type))
          else:
            if weights[u][1] > weight + time + 5:
              weights[u][1] = weight + time + 5
              Q.append((weights[u][1], u, time, type))
        else:
          if weights[u][type] > weight + time + 20:
            weights[u][type] = weight + time + 20
            Q.append((weights[u][type], u, time, type))

  return min(weights[B])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
