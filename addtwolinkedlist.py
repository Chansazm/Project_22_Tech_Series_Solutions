#Create a node object
class Node(object):
    def __init__(self,x):
        self.value = x
        self.next = None
        
#create a class solution
class solution:
    def addtwolists(self,l1,l2):
        return self.addtwohelper(l1,l2,0)
    
    def addtwohelper(self,l1,l2,c):
        pass
        


# Create a driver program and print
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = solution.addtwolists(l1,l2)
while answer:
    print(answer.value)
    answer = answer.next