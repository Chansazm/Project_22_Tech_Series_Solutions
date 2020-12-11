class solution(object):
    def reconstruct(self,nums):
        nums.sort(key = lambda x:(-x[0],x[1]))
        
        res = []
        for person in nums:
            res.insert(person[1],person)
        return res



nums = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(solution().reconstruct(nums))