def lis(arr):
    cache = [1] * len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and cache[i] < cache[j] +1:
                cache[i] = max(cache[i],cache[j]+1)
    return max(cache)
    
 
#Driver function
#5
print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3]))

#Recursive Solution
T = dict()
def Rlis(A,i):
    if i not in T:
        T[i] = 1
        for j in range(i):
            if A[j] < A[i]:
                T[i] = max(T[i],Rlis(A,j) + 1)
    return T[i]

A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3]
print(max(Rlis(A, i) for i in range(len(A))))

