"""
Pewien podróznik chce przebyc trase z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy.Wbaku miesci
sie dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawedzie to
łaczace je drogi. Kazda krawedz ma długosc w kilometrach (przedstawiona jako licza naturalna). W kazdym
wierzchołku jest stacja benzynowa, z dana cena za litr paliwa. Prosze podac algorytm znajdujacy trase z
punktu A do punktu B o najmniejszym koszcie.

"""
from math import inf
from queue import PriorityQueue

def Dijskra(G,PetrolStation,CapasityOfFuel,CurrentAmountOfFuel,start,end):
    n = len(G)
    Cost = [[inf for i in range(CapasityOfFuel+1)] for i in range(n)]
    pq = PriorityQueue()
    Cost[start][CurrentAmountOfFuel] = 0
    pq.put((0,CurrentAmountOfFuel,start))

    while not pq.empty():
        value, fuel, vertex = pq.get()
        for v,weight in G[vertex]:
            for d in range(0,CapasityOfFuel -CurrentAmountOfFuel +1):
                if weight <= d + fuel and Cost[v][d + fuel - weight] > Cost[vertex][fuel] + d * PetrolStation[vertex]:
                    Cost[v][d + fuel - weight] = Cost[vertex][fuel] + d * PetrolStation[vertex]
                    pq.put((Cost[v][d + fuel - weight],d + fuel - weight,v))
        if vertex == end:
            return Cost
    return Cost

def Cost_of_travel(G,PetrolStation,CapasityOfFuel,CurrentAmountOfFuel,start,end):
    cost = Dijskra(G,PetrolStation,CapasityOfFuel,CurrentAmountOfFuel,start,end)

    minCost = inf

    for price in cost[end]:
        if minCost > price:
            minCost = price
    if minCost != inf:
        return minCost
    else:return None