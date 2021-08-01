class solution(object):
    def twoSum(self, nums,target):
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target:
                    return i1,i2
        return []

#######################################################
class solutionb(object):
    def twosumB(self,nums,target):
        values = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i,values[diff]] 
            values[num] = i
        return []

 #######################################################
print(solution().twoSum([1,3,5,6,7,9],8))
print(solutionb().twosumB([1,3,4,5],9))
                 