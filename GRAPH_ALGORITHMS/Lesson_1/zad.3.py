"""
Dany jest graf G = (V,E), którego wierzchołki reprezentuja punkty
nawigacyjne nad Bajtocja, a krawedzie reprezentuja korytarze powietrzne miedzy tymi punktami. Kazdy
korytarz powietrzny ei > E powiazany jest z optymalnym pułapem przelotu pi > N (wyrazonym w metrach).
Przepisy dopuszczaja przelot danym korytarzem jesli pułap samolotu rózni sie od optymalnego najwyzej o t
metrów. Prosze zaproponowac algorytm (bez implementacji), który sprawdza czy istnieje mozliwosc przelotu
z zadanego punktu x > V do zadanego punktu y > V w taki sposób, zeby samolot nigdy nie zmieniał pułapu.

"""


def DFS(G,visited,path,start,meta,height,pulap):

    visited[start] = True
    path.append(start)

    if start == meta:
        print(path)

    else:

        for v , wysokosc in G[start]:
            if abs(wysokosc - height) < pulap and visited[v] == False:

                DFS(G, visited, path, v, meta, wysokosc, pulap)

    path.pop()
    visited[start] = False