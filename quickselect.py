def quickselect1(data,k):
    for i in range(0,k):
        for j in range(0,k):
            data = data[:]

def quickselect0(arr,k):
    return sorted(arr)[-k]

def partition(arr,low,high):
    pivot = arr[high]
    i = low
    for j in range(len(arr)):
        if arr[i] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[i],arr[high] = arr[i],arr[high]
    return i
        

def quickselect(arr,k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        pivot_index = partition(arr,left,right)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
    return -1









print(quickselect([8,7,2,3,4,1,5,6,9,0],4))