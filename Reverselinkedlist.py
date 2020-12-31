class Node(object):
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
    def __repr__(self):
        res = str(self.value)
        if self.next:
            res += str(self.next)
        return res
    
class solution(object):
    def reverse(self,node):
        current = node
        Previous = None
        
        while current != None:
            temp = current.next
            current.next = Previous
            Previous = current
            current = temp
            
        return Previous
        
node = Node(1,Node(2,Node(3,Node(4,Node(5)))))
print(solution().reverse(node))
