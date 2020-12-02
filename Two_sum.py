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