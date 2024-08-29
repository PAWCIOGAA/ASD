
def Maxsum_optimal(A):
    n = len(A)
    max_sum = A[0]
    last_sum = A[0]
    for i in range(1,n):
        max_sum = max(max_sum,last_sum + A[i],A[i])
        last_sum = max(last_sum + A[i],A[i])
    return max_sum


A = [-2,1,-3,4,-1,2,1,-5,4]

print(Maxsum_optimal(A))