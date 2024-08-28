from egz1atesty import runtests

def Graph_convert(M):
  maxi = max(max(u,v) for u,v,weight in M)
  G = [[] for _ in range(maxi+1)]
  for u,v,weight in M:
    G[u].append((v,weight))
    G[v].append((u,weight))

  return G,maxi+1

def B_convert(B,n:'number of vertices'):
  new_B = [[] for _ in range(n)]
  index = 1
  for i,p,q in B:
    new_B[i].append((index,p/q))
    index += 1

  return new_B

from math import inf,floor
from queue import PriorityQueue

def Dijaskra(G,B,m,start):
  n = len(G)
  weights = [[inf]*(m+1) for _ in range(n)] # [i][0]- na piechotę, reszta to rowery
  weights[0][0] = 0
  PQ = PriorityQueue()
  PQ.put((0,1,0,start)) # czasCałkowity , 0 = na piechotę reszta to jakiś rower,mnożnik, vertex

  while not PQ.empty():
    time, mnoznik,bike, vertex = PQ.get()
    if time > weights[vertex][bike]:
            continue
    for v, weight in G[vertex]:
      if bike == 0:
        if weights[v][0] > time + weight:
            weights[v][0] = time + weight
            PQ.put((weights[v][0],1,0,v))
        for index,rate in B[vertex]:
          new_time = time + (weight * rate)
          if weights[v][index] > new_time:
            weights[v][index] = new_time
            PQ.put((weights[v][index], rate, index, v))
      else:
        new_time = time + (weight * mnoznik)
        if weights[v][bike] > new_time:
            weights[v][bike] = new_time
            PQ.put((weights[v][bike],mnoznik, bike, v))
  return weights
def armstrong( B, G, s, t):
  # tu prosze wpisac wlasna implementacje

  G,maxi = Graph_convert(G)
  m = len(B)
  B = B_convert(B,maxi)

  weights = Dijaskra(G,B,m,s)

  result = min(weights[t])

  result = floor(result)

  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
