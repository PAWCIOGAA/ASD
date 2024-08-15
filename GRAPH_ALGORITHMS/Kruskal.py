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

def kruskal(G:'(V,E)'):
    V,E = G
    E.sort(key = lambda x:x[2])

    vertex = [make_set(v) for v in V]

    result = []
    for edge in E:
        u, v, weight = edge
        if not connected(vertex[u],vertex[v]):
            union(vertex[u],vertex[v])
            result.append(edge)
    return result
