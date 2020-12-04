class solution(object):
    def twoSum(self, nums,target):
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target:
                    return i1,i2
        return []

    def twoSumB(self,nums,target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []

print(solution().twoSumB([1,3,4,5],9))

#######################################################
class solution(object):
    """def twosum(self,nums,target):
        for k, v in enumerate(nums):
            for j, v2 in enumerate(nums):
                if v == v2:
                    continue
                if v + v2 == target:
                    return k,j
        return []"""

    def twosumB(self,nums,target):
        values = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i,values[diff]] 
            values[num] = i
        return []

 

#print(solution().twosum([1,3,5,6,7,9],8))
print(solution().twosumB([1,3,4,5],9))
                 