class solution:
    def getRange(self,arr,target):
        first = self.binarysearch(arr,0,len(arr) - 1,target, True)
        Last = self.binarysearch(arr,0,len(arr) - 1,target, False)
        return[first,Last]
    
    def binarysearch(self,arr,low,high,target,findfirst):
        if high < low:
            return -1
        mid = low + (high - low)/2
        
    
    
    
    
arr = [1,2,4,5,7,9,9,6]
x = 9
print(solution().getRange(arr,x))