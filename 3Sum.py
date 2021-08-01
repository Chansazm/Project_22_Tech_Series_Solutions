class solution:
    def threesum(self, nums):
        result = []
        for i1 in range(0, len(nums)):
            for i2 in range(i1+1, len(nums)):
                for i3 in range(i2+1, len(nums)):
                    a, b, c = nums[i1], nums[i2], nums[i3]
                    if a + b + c == 0:
                        result.append([a, b, c])
        return result

    def threesumindices(self, nums):
        nums.sort
        result = []
        for i in range(len(nums)):
            self.twosumindices(nums, i, result)
        return result

    def twosumindices(self, nums, start, result):
        low = start + 1
        high = len(nums)-1
        while low < high:
            sum = nums[start] + nums[low] + nums[high]
            if sum == 0:
                result.append([nums[start], nums[low], nums[high]])
                low += 1
                high -= 1
            elif sum < 0:
                low += 1
            else:
                high -= 1
        return result


# print(solution().threesum([-1,0,1,2,-4,-3]))
print(solution().threesumindices([-1, 0, 1, 2, -4, -3]))
