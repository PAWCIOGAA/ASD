# W Algorytmie korzystam z algorytmu Kruskala.
# Na początku tworzę graf pełny w postaci listy krawędzi o krawędziach ważonych
# o wagach wyliczonych z podanego w zadaniu wzoru. Krawędzie sortuje rosnąco według wag.
# Następnie w pętli wyznaczam minimalne drzewo rozpinające stworzonego grafu, sprawdzam
# i aktualizuje minimum ( minimalną liczbę dni będącą wynikiem ) oraz usuwam najmniejszą krawędź.
# Robię to dopóki graf jest spójny. Kiedy graf przestaje być spójny zwracam wynik

from math import ceil
import math
def Create_graf(A,n):
    G = []

    for i in range(n):
        for j in range(i + 1,n):
            len = math.sqrt((A[i][0] - A[j][0]) * (A[i][0] - A[j][0]) + (A[i][1] - A[j][1]) * (A[i][1] - A[j][1]))
            len = math.ceil(len)
            G.append((i,j,len))
            G.append((j,i,len))
    return G

class Node:
    def __int__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0
def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:return
    if x.rank < y.rank:
        x.parent =y
    else:
        y.parent = x
        if x.rank == y.rank: x.rank += 1
def make_set(x:'id'):
    return Node(x)

def connected(x,y):
    return find(x) == find(y)
def Kruskal(G,A):
    n = len(A)
    vertex = [make_set(v) for v in range(n)]

    result = []

    for edge in G:
        a,b,c = edge
        if not connected(a,b):
            union(a,b)
            result.append(edge)
    if len(result) == n-1:
        return abs(result[0][2] - result[-1][2])
    else: return float('inf')

def highway( A ):
    n = len(A)
    G = Create_graf(A,n)
    wynik = float('inf')

    m = len(G)
    G.sort(key= lambda x:x[2])

    for i in range(m-n):
        wynik = min(Kruskal(G[i:],A),wynik)


    return None if wynik == float("inf") else wynik


    # tu prosze wpisac wlasna implementacje



# zmien all_tests na True zeby uruchomic wszystkie testy
