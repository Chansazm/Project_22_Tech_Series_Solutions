def Maxsubarray(arr):
    sum = 0
    Max_Sum = 0
    for n in arr:
        sum += n
        if sum < 0:
            sum = 0
        else:
            Max_Sum = max(Max_Sum,sum)
    return Max_Sum




print(Maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
#6