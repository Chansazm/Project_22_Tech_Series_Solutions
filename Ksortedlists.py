class Node(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ''
            c = c.next
        return answer
    
def merge(lists):
    arr = []
    for node in lists:
        while node:
            arr.append(node.val)
            node = node.next
    head = root = None
    for val in sorted(arr):
        if not root:
            head = root = Node(val)
        else:
            root.next = Node(val)
            root = root.next
    return head

def merge2(lists):
    head = current = Node(-1)
    while any(lists is not None for list in lists):
        pass
    return head.next
    
    
a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(a)
# 135
print(b)
# 246
print(merge([a, b]))
# 123456