from egzP3btesty import runtests 
from queue import PriorityQueue

class Node:
    def __init__(self, id):
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
    if x ==y:return
    if x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x
        if x.rank == y.rank: x.rank += 1

def make_set(x:'id'):
    return Node(x)

def Connected(x,y):
    return find(x) == find(y)

def Graph_convert(M):
    n = len(M)
    edge_list = []
    suma = 0
    for i in range(n):
        for u,weight in M[i]:
            if i < u:
                edge_list.append((i,u,weight))
                suma += weight
    return n,suma,edge_list


def lufthansa ( G ):
    #tutaj proszę wpisać własną implementację
    n,Sum_of_all_edges,G = Graph_convert(G)
    G.sort(key = lambda x:x[2],reverse = True)

    vertex = [make_set(v) for v in range(n)]
    maximum_left_edge = -float('inf')
    suma = 0
    for edge in G:
        u,v,weight = edge

        if not Connected(vertex[u],vertex[v]):
            union(vertex[u],vertex[v])
            suma += weight
        else:
            maximum_left_edge = max(maximum_left_edge,weight)


    result = Sum_of_all_edges-(suma + maximum_left_edge)
    return result

runtests ( lufthansa, all_tests=True )