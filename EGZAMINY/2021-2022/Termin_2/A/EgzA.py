from queue import PriorityQueue
from egz2atesty import runtests

# O(n^2logn) xd

def coal(A,T):
    n = len(A)
    DP = []
    PQ = PriorityQueue()

    for i in range(n):
        PQ.put((i,T))

    last = -1
    for i in range(n):

        index, weight = PQ.get()

        while weight - A[i] < 0:
            if weight > 0:
                DP.append((index,weight))
            index, weight = PQ.get()

        PQ.put((index,weight - A[i]))
        last = index

        for tuple in DP:
            PQ.put(tuple)

        DP = []

    return last

runtests(coal, all_tests=True)