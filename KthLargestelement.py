import heapq

def findKthlargest(nums,K):
    return sorted(nums)[len(nums)-K]

def findKthlargest2(nums,K):
    return heapq.nlargest(K,nums)[-1]

def quickselect(arr,k):
    k = len(arr) - k
    left = 0
    right = len(arr) - 1
    
    while left < right:
        pivot_index = partition(arr,left,right)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
    return -1

def partition(arr,low,high):
    pivot = arr[high]
    i = low
    for j in range(low,high):
        if pivot <= arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[high],arr[i] = arr[i],arr[high]
    return i
        
         
    
        
        
            
            
     
    

print(findKthlargest2([3,5,2,4,6,8],3))
print(quickselect([3,5,2,4,6,8],3),4)