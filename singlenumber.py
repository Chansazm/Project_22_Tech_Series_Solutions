def singlenumber(nums):
    map = {}
    for i in nums:
        map[i] = map.get(i,0) 
    for i,v in enumerate(map):
        print(i,v)
singlenumber([4, 3, 2, 9, 1, 3, 2])
        