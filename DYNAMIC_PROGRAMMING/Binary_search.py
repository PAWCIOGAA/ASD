def Binary_search(A,left,right,key): # na początku left = 0 ,a right = len(A) - 1
    while(right-left > 1):
        m = left + (right - left) //2
        if(A[m] >= key):
            right = m
        else:
            left = m
    return right