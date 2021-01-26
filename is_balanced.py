class Node(object):
    def __init__(self,value,left=None,right=None):
        self.val = value
        self.left = left
        self.right = right
    
class solution(object):
    #returns is_balanced and height
    def _is_balanced_helper(self,n):
        if not n:
            return (True,0)
        lbalanced,lheight = self._is_balanced_helper(n.left)
        rbalanced,rheight = self._is_balanced_helper(n.right)
        return (lbalanced and rbalanced and abs(lheight-rheight) <= 1,
                max(lheight,rheight)+1)
    def is_balanced(self,n):
        return self._is_balanced_helper(n)[0]
        


#driver function

n = Node(1)
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)
#               1
#              / \
#             2   3
#            /
#           4
print(solution().is_balanced(n))