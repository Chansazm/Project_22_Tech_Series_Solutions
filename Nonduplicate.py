class solution(object):
    def nonduplicate(self,nums):
        results = {}
        for n in nums:
            results[n] = results.get(n,0) + 1
        for key, value in results.items():
            if value == 1:
                return key
        return False

    def nonduplicate2(self,nums):
        unique = 0
        for n in nums:
            unique ^= n
        return unique
    
    
    
    #driver function
    #return true if number is one
    #time complexity is O(n), space complexity is O(n)
#print(solution().nonduplicate([2,4,6,1,2,4,6]))
print(solution().nonduplicate2([2,4,6,1,2,4,6]))