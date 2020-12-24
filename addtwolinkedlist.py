class Node(object):
    def __init__(self,x):
        self.value = x
        self.next = None
        
        
class Solution(object):
    def addtwo(self,l1,l2):
        
        return None
    

l1 = Node(2)
l1 = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2 = Node(6)
l2.next.next = Node(4)


answer = Solution().addtwo(l1,l2)
while answer:
    print(answer.value)
    answer = answer.next
        