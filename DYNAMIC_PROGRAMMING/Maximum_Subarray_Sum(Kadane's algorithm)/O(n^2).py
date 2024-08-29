from math import inf
def Better_Bruteforce(A):
    n = len(A)
    max_sum = -inf
    for i in range(n):
        temp_sum = 0
        for j in range(i,n):
            temp_sum += A[j]
            if temp_sum > max_sum:
                max_sum = temp_sum

    return max_sum

A = [-2,1,-3,4,-1,2,1,-5,4]

print(Better_Bruteforce(A))