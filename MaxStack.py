class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.max = []
    
    def push(self,val):
        self.stack.append(val)
        if self.max and self.max[-1] > val:
            self.max.append(self.max[-1])
        else:
            self.max.append(val)
    
    def pop(self):
        if self.max:
            self.max.pop()
        if self.stack:
            return self.stack.pop()
    
    def _isempty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.max)
            
    
    def max(self):
        return self.max[-1]
    
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)



"""
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
    """