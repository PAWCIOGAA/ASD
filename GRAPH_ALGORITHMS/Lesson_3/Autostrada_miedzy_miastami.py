#Budujemy autostradę między miastami -
#wierzchołki to miasta, krawędzie to
#autostrada. Waga krawędzi to czas budowy
#danego kawałka autostrady. Chcemy przejechać
#między wszystkimi miastami, ale też zminimalizować
#okres między otwarciem pierwszego, a ostatniego
#kawałka. Szukamy tych krawędzi. Pomysł: budujemy
#MST dla m ciągów "najcięższych" krawędzi -
#najpierw sortujemy krawędzie, później wykonujemy
#Kruskala i badamy różnicę między najmniejszą
#a największą wagą.


# w tym zadaniu chodzi tylko i wyłącznie o to aby różnica pierwszej i ostatniej krawędzi MST była jak najmniejsza
#tak naprawdę nie szukamy tutaj mst tylko tej najmniejszej różnicy
# algorytm kruskala ktróy znajduje mst nam  w tym pomaga ale modyfikujemy go poprzez usuwanie krawędzi w grafie

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
from math import inf
def kruskal(G:'(V,E)',n:'liczba wierzchołków(MST ma v-1 krawędzi zawsze)'):
    V,E = G
    E.sort(key = lambda x:x[2])

    vertex = [make_set(v) for v in V]

    result = []
    for edge in E:
        u, v, weight = edge
        if not connected(vertex[u],vertex[v]):
            union(vertex[u],vertex[v])
            result.append(edge)
        if len(result) < n-1: return result,inf
        else: return result,(result[-1][2] - result[0][2])

def MinimumDifference(G,n):
    MinResult,MinDifference = [], inf

    for i in range(1,len(G)):
        result,difference = kruskal(G[i:],n)

        if difference < MinDifference:
            MinResult = result
            MinDifference = difference

    if MinDifference == inf: return "Not Coherend"
    return MinResult,MinDifference


