class Node(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        n = self
        ret = ''
        while n:
            