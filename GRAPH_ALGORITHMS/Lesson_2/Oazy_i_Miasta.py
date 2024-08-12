"""
Oazy i miasta
mamy panstwo

te miasta maja bramy na polnocy i poludniu
miedzy miastami znajduja sie oazy
z miast wychodza drogi na polnoc i poludnie i przechodzi przez jakies oazy
w reulach panstwa, w przypadku wjazdu do miasta jedna bramu, musimy wyjechac druga
istnie problem, bo mamy czlowieka, ktory chce odwiedzic wszystkie miasta dokladnie raz
jesli goniec wjedzie od polnocy, to musi wyjechac od poludnia
wyjezdza ze stolicy i wraca do stolicy druga droga.

narzuca sie ze miasto to krawedz skierowana, w dwie strony, a cala ta przestrzeń ( te krawedzie ) zamienic na wierzcholek
mamy wiec problem znalezienia cykl eulera, a nie cyklu hamiltona.
nie musza byc jednak krawedzie skierowane

jak zamienic krawedzie ( te oazy, te duze przestrzenie ) na wierzcholek


"""

def DFS_oaza(G):
    n = len(G)
    visited = [False for i in range(n)]
    city = []
    def DFS_visit(G,u):
        visited[u] = True
        if G[u][0] == 'O':
            for v in G[u][1]:
                if not visited[v]:
                    DFS_visit(G,v)
        else: city.append(u)

    Gr = []

    for i in range(n):
        if G[i][0] == 'O' and not visited[i]:
            DFS_visit(G,i)
            for i in range(len(city)):
                visited[city[i]] = False
            Gr.append(city)
            city = []

    edges = [[] for i in range(len(Gr))]
    for i in range(len(Gr)):
        for j in range(len(Gr[i])):
            city  = Gr[i][j]
            for k in range(len(Gr)):
                if (k != i and city in Gr[k]) or found(Gr[k],G[city][1]):
                    edges[i].append(k)
                    break

    return Has_Euler_cycle(edges)



def found(tab1,tab2):
    n = len(tab1)
    for i in range(n):
        if tab1[i] in tab2: return True
    return False
def Has_Euler_cycle(G):
    n = len(G)
    for i in range(n):
        if len(G[i])%2 != 0:return False
    return True


