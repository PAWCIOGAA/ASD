def MapCars(A,L):
    n = len(A)
    total = 0
    for i in range(n):
        total+= A[i]
        if total > 2*L:
            return i - 1

    return n - 1


def Dwa_Pasy(A,L):
    Last_car_index = MapCars(A,L)

    DP = [ [ [None]*(L+1) for _ in range(L+1)] for _ in range(Last_car_index+1)]
    Parents = ['']*len(A)
    def Recurs(i:'car index',l:'remaining place on the left line',r:'remaining place on the right line'):
        if l < 0 or r < 0: return False

        if i == 0:
            if l>=A[0]:
                Parents[0] = 'L'
                return True
            if r >= A[0]:
                Parents[0] = 'R'
                return True
            return False

        if DP[i][l][r] is None:
            if Recurs(i-1,l-A[i],r):
                Parents[i] = 'L'
                DP[i][l][r] = True
            elif Recurs(i-1,l,r-A[i]):
                Parents[i] = 'R'
                DP[i][l][r] = True
        return DP[i][l][r]
    for i in range( Last_car_index, -1, -1):
        if Recurs(i, L, L):
            return i + 1, Parents
    return -1, []