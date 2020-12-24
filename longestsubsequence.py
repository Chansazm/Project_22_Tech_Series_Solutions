def lis(arr):
    cache = [1] * len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i],cache[j]+1)
    return max(cache)
    
    


#Driver function
#5
print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3]))