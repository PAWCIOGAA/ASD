from egz2atesty import runtests

def dominance(T):
    n = len(T)
    max_x = max(T,key=lambda p:p[0])[0]
    max_y = max(T,key=lambda p:p[1])[1]

    Greater_y = [0]*(max_y+1)
    Smaller_x = [0]*(max_x+1)
    Equal_x = [0]*(max_x+1)


    for x, y in T:
        Greater_y[y] += 1
        Smaller_x[x] += 1
        Equal_x[x] += 1

    for x in range(1,max_x+1):
        Smaller_x[x] += Smaller_x[x-1]
    for y in range(max_y-1,-1,-1):
        Greater_y[y] += Greater_y[y+1]


    dominance_max = 0
    for x,y in T:
        dominance_max = max(dominance_max,Smaller_x[x] - Greater_y[y] - Equal_x[x] + 1)

    return dominance_max

runtests( dominance, all_tests = True)