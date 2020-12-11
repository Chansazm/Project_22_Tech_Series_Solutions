from collections import defaultdict

class solution(object):
    def ransom(self,magazine,note):
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1
        for c in note:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
      
        return True
    
    
    
    
    


#driver function
print(solution().ransom(['a','b','c','d','e'],'bed'))