class solution(object):
    def checkpossibility(self,nums):
        invalid_index = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if invalid_index != -1:
                    return False
                invalid_index = i
        if invalid_index == 0:
            return True
        if invalid_index == len(nums) - 2:
            return True
        if nums[invalid_index] == nums[invalid_index + 2]:
            return True
        if nums[invalid_index - 1] < nums[invalid_index + 1]:
            return True
                     
        return False
    
    
    
    

#Driver function
print(solution().checkpossibility([4,1,2])) #True