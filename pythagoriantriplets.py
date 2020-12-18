def pythagorian(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if a*a + b*b == c*c:
                    return True
    return False

def pythagorianset(nums):
    data = set([n*n for n in nums])
    for a in nums:
        for b in nums:
            if a*a + b*b in data:
                return True
    return False

#Driver function
print(pythagorian([1,3,9,4,5,12,1]))
print(pythagorianset([1,3,9,4,5,12,1]))