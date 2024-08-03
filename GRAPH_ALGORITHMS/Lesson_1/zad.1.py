"""
Dany jest graf G = (V,E), gdzie kazda krawedz ma wage ze zbioru
{1, . . . , E} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych wierzchołków
x i y sprawdza, czy istnieje sciezka z x do y, w której przechodzimy po krawedziach o coraz mniejszych wagach.

Dodatkowy argument, ktory mowi o wadze ostatniej krawedzi.
Robimy przeszukanie dla wszystkich krawedzi, ktore maja wage mniejsza
Nie mamy visted, mozemy wchodzic do wierzcholkow kilka razy
Nie zapetlimy sie, nie cofniemy sie, bo wchodzimy do krawedzi o MNIEJSZEJ wadze
Wagi sa tez parami rozne

"""

# Rozwiązanie DFS


def DFS(G,x,y,weight):


        for v in G[x]:
            if weight[x] > weight[v]:
                if v == y:
                    return True
                if DFS(G,v,y,weight):
                    return True


        return False

# Rozwiązanie BFS
from queue import Queue
def BFS(G,x,y,weight):
    Q = Queue()
    Q.put(x)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if v == y and weight[u]> weight[v]:
                return True
            if weight[u]> weight[v]:
                Q.put(v)
    return False






G = [[1],[0,2,3,6,10],[1],[1,6,4],[3,5],[4,8,9],[1,3,7],[6,8],[7,5,12,9],[5,8,12],[1,11],[10,12],[11,8,9]]
weight = [100,99,53,11,5,934,235,11,634,34,98,97,96]

B = [[1],[0,2],[1]]
weight_1 = [10,9,12]
print(BFS(B,0,2,weight_1))