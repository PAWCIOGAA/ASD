
from egz3btesty import runtests

def maze(A):
    n = len(A)
    DPG = [[-1]*n for _ in range(n)]
    DPD = [[-1] * n for _ in range(n)]
    DPD[0][0],DPG[0][0] = 0,0

    for i in range(1,n):
        if A[i][0] != '#':
            DPD[i][0] = DPD[i-1][0] + 1
        else:break


    for col in range(1,n):
        for row in range(n):
            if A[row][col] != '#':
                if A[row][col-1] == '#': continue
                value = max(DPD[row][col-1],DPG[row][col-1]) + 1
                DPG[row][col],DPD[row][col] = value,value

        for row in range(n):
            if A[row][col] =='#': continue
            if A[row][col - 1] == '#': continue

            row1,row2 = row-1,row+1

            while row1 >= 0:
                if A[row1][col] == '#': continue
                if A[row1][col - 1] == '#': continue

                DPG[row1][col] = max(DPG[row1][col],DPG[row1+1][col]+1)
                row1 -= 1

            while row2 < n:
                if A[row2][col] == '#': continue
                if A[row2][col - 1] == '#': continue

                DPD[row2][col] = max(DPD[row2][col], DPD[row2 - 1][col] + 1)
                row1 += 1
    if DPG[n - 1][n - 1] == -1 and DPD[n - 1][n - 1] == -1: return -1
    return max(DPG[n - 1][n - 1], DPD[n - 1][n - 1])



runtests( maze, all_tests = True )