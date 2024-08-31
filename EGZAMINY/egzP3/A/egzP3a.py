from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def Knapsack(fundusze,koszt,wyborcy):
    DP = [[0]*(fundusze+1) for _ in range(len(koszt))]
    for i in range(fundusze + 1):
        if i >= koszt[0]:
            DP[0][i] = wyborcy[0]

    for i in range(1,len(koszt)):
        for j in range(fundusze+1):
            if koszt[i] <= j:
                DP[i][j] = max(DP[i-1][j],DP[i-1][j - koszt[i]] + wyborcy[i])
            else:
                DP[i][j] = DP[i-1][j]

    return DP[len(koszt)-1][fundusze]



def wybory(T):
    #tutaj proszę wpisać własną implementację
    suma = 0
    for el in T:
        S = el.fundusze
        P = []
        W = []
        pp = el
        while pp != None:
            P.append(pp.wyborcy)
            W.append(pp.koszt)
            pp = pp.next
        suma += Knapsack(S,W,P)
    return suma


    return 0

runtests(wybory, all_tests = True)