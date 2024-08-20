# Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z
# alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo
# W = W[0], . . . ,W[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować
# funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki
# układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki).
# Jeśli takiej ścieżki nie ma, należy zwrócić -1.

# Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para
# (L, E). L to lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku i. E jest listą krawędzi
# i każdy jej element jest trójką postaci (u, v, w), gdzie u i v to wierzchołki
# połączone krawędzią o wadze w.

# Przyklad.

# W reprezentacji przyjętej w zadaniu mógłby być zapisany jako:

# L = ["k","k","o","o","t","t"]
# E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
# G = (L,E)

# Rozwiązaniem dla tego grafu i słowa W = "kto" jest 4 i jest osiągane przez ścieżkę 1 − 4 − 3. Inna
# ścieżka realizująca to słowo to 1 − 4 − 2, ale ma koszt 8


from zad2testy import runtests
from queue import PriorityQueue
from math import inf

def Convert(E,n):

    G = [ [] for _ in range(n)]

    for u,v,weight in E:
        G[u].append((v,weight))
        G[v].append((u,weight))
    return G
def Dijskra(G,A,W):
    n = len(G)
    m = len(W)
    weights = [[inf] * m for _ in range(n)]
    pq = PriorityQueue()
    for u in range(len(A)):
        if A[u] == W[0]:
            weights[u][0] = 0
            pq.put((0, u,0)) # weight, vertex, letter index

    while not pq.empty():
        waga, u, index = pq.get()

        if index == m-1: return waga

        for v,weight in G[u]:
            if weights[v][index + 1]>= waga + weight and A[v] == W[index + 1]:
                weights[v][index + 1] = waga + weight
                pq.put((weights[v][index + 1],v,index + 1))
    return -1


def letters(G,W):
    A,E = G
    m = len(A)
    E = Convert(E,m)

    return Dijskra(E,A,W)





runtests(letters)
