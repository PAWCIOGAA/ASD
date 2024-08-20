from zad7testy import runtests


def ispath(G, u, path, n, visited, gate):
    # Sprawdzamy, czy ścieżka odwiedziła już wszystkie miasta i czy ostatnie miasto
    # może wrócić do pierwszego miasta przez odpowiednią bramę.
    if len(path) == n:
        if path[0] in G[u][gate]:
            return True
        else:
            return False

    for v in G[u][gate]:
        if not visited[v]:
            visited[v] = True
            path.append(v)
            next_gate = 0 if u not in G[v][0] else 1
            if ispath(G, v, path, n, visited, next_gate):
                return True
            visited[v] = False
            path.pop()

    return False


def droga(G):
    n = len(G)

    for start in range(n):
        visited = [False] * n
        path = [start]
        visited[start] = True
        if ispath(G, start, path, n, visited, 0):
            return path
        if ispath(G, start, path, n, visited, 1):
            return path
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
