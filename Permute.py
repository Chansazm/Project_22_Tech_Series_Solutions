class solution(object):
    def _permuteHelper(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]

        result = []
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            result += self._permuteHelper(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
        return result

    def permute(self, nums):
        return self._permuteHelper(nums)
    
    def permute2(self,nums,values=[]):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            result += self.permute2(nums[:i][:i+1],values + [nums[i]])
        return result


# driver function
#print(solution().permute([1, 2, 3]))
print(solution().permute2([1, 2, 3]))
