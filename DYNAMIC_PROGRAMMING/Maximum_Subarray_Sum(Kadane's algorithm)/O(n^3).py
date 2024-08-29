from math import inf
def BrutForce(A):
    n = len(A)
    max_sum = -inf
    temp_sum = 0
    for i in range(n):
        for j in range(i,n):
            temp_sum = 0
            for k in range(i,j):
                temp_sum += A[k]
            if max_sum < temp_sum:
                max_sum = temp_sum


    return max_sum


A = [-2,1,-3,4,-1,2,1,-5,4]

print(BrutForce(A))