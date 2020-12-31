from collections import _heapq ,defaultdict



class solution(object):
    def topkfrequent(self,nums,k):
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            
        
        return [count]
    
    

#Driver function
print(solution().topkfrequent([1,1,1,2,2,3],2))