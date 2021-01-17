class Node(object):
    def __init__(self,value,next):
        self.value = value
        self.next = next
    
    def __str__(self):
        n = self
        answer = ''
        while n:
            answer += str(n.value)
            n = n.next
        return answer
        


def removekth(node,k):
    slow, fast = node, node
    for i in range(k):
        fast = fast.next
    if not fast:
        return Node.next

    previous = None
    while fast:
        previous = slow
        fast = fast.next
        slow = slow.next
    previous.next = slow.next
    return Node
    

#Driver function
head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(head)
# 12345

head = removekth(head, 1)
print(head)
# 1234