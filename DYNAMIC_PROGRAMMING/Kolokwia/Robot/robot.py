from queue import PriorityQueue
def robot(L,A,B):
    n = len(A)
    m = len(A[0])

    DP = [[[[-1]*3 for _ in range(4)]for _ in range(m)] for _ in range(n)]

    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    PQ = PriorityQueue()
    PQ.put((0,A[0],A[1],0,0)) # time,x ,y ,direction ,tempo

    seconds = [60,40,30]

    while not PQ.empty():
        time,x,y,direction,tempo = PQ.get()
        if (x,y) == B:
            return time

        if DP[y][x][direction][tempo] != -1 or L[x][y] == 'X': continue
        DP[y][x][direction][tempo] = time

        PQ.put((time + 45,x,y,(direction +1)%4,0))
        PQ.put((time + 45, x, y, (direction + 3) % 4, 0))
        x += moves[direction][0]
        y += moves[direction][1]

        PQ.put((time + seconds[tempo],x,y,direction,min(tempo+1,2)))

    return None