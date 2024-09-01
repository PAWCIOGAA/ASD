from egzP4atesty import runtests 

def BinarySearch(T,L,R,key):
    while R - L > 1:
        m = L + (R-L)//2
        if T[m] >= key:
            R = m
        else:
            L = m
    if key < T[0]:
        return 0

    return R






def LIS(T):
    n = len(T)
    S = []
    S.append(T[0])
    for i in range(1,n):
        if T[i] >= S[len(S)-1]:
            S.append(T[i])
        else:
            S[BinarySearch(S,0,len(S)-1,T[i])]  = T[i]
    return len(S)




def mosty ( T ):
    #tutaj proszę wpisać własną implementację

    T.sort(key = lambda x:(x[0],x[1]))
    n = len(T)
    T2 = [T[i][1] for i in range(n)]

    return LIS(T2)

runtests ( mosty, all_tests=True )