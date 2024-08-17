# Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
# Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wykonanie zadania a musi poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2 zadanie b
# musi być wykonane wcześniej, a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaimplementować funkcję tasks(T), która dla danej tablicy T, zwraca tablicę z kolejnymi numerami
# zadań do wykonania.
# Przykład Dla tablicy T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ] wynikiem
# jest tablica [1,0,2,3].

#Topological sort

def Convert(M):
    n = len(M)
    G = [[] for _ in range(n)]
    for a in range(n):
        for b in range(a+1,n):
            if M[a][b] == 1:
                G[a] += [b]
            elif M[a][b] == 2:
                G[b] += [a]
    return G


def TopologicalSort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = []
    def dfs(G,s):
        if not visited[s]:
            for v in G[s]:
                if not visited[v]:
                    visited[v] = True
                    dfs(G,v)
            result.append(s)
    for u in range(n):
        if not visited[u]:
            dfs(G,u)
    result.reverse()
    return result


