from egzP5atesty import runtests 

def inwestor ( T ):
    #tutaj proszę wpisać własną implementację
    n = len(T)
    LS = [-1]*n
    RS = [n] * n
    stack = [-1,0]

    for i in range(1,n):
        while T[i] < T[stack[len(stack)-1]] and stack[len(stack) -1 ] != -1:
            RS[stack[len(stack)-1]] = i
            stack.pop()

        if T[i] == T[i-1]:
            LS[i] = LS[i-1]
        else:
            LS[i] = stack[len(stack)-1]
        stack.append(i)
    max_area = -1
    for j in range(n):
        max_area = max(max_area, T[j] *(RS[j] - LS[j] -1))
    return max_area

runtests ( inwestor, all_tests=True )