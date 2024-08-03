# Dana jest szachownica o wymiarach n × n. Kazde pole (i, j)
# ma koszt (liczbe ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
# szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
# minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
# sciezki króla

from queue import PriorityQueue
def Kings_path(G):
    n = len(G)
    Q = PriorityQueue()
    def IsPossibleToMove(moves ,x,y):
        for move in moves:
            if (x,y)  + move >= n or (x,y)  + move < 0:
                return False
        return True


    distance = [[float('inf') for i in range(n)] for i in range(n)]
    moves = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
    distance[0][0] = 0
    Q.put((1,(0,0)))

    while not Q.empty():
        counter, vertex = Q.get()
        x,y = vertex

        if counter == 1:

            for move in moves:
                xTo, yTo = move
                if (xTo + x >=0 and xTo + x < n) and (yTo + y >=0 and yTo + y < n) and distance[x][y] + G[xTo][yTo] < distance[xTo+ x][yTo + y]:
                    distance[xTo + x][yTo + y] = distance[x][y] + G[xTo][yTo]
                    Q.put((G[xTo+ x][yTo + y],(xTo+ x,yTo + y)))

            if xTo+ x == n-1and yTo + y == n-1:
                return distance[n-1][n-1]

        else:
            Q.put((counter-1,vertex))

