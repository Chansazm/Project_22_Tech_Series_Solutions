class Node(object):
    def __init__(self,value,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
class Solution(object):
    def _isvalidBSTHelper(self,n,low,high):
        #Base Case ,because no node is still considered a valid BST
        if not n:
            return True
        #Recursively call _isvalidBSTHelper
        value = n.value
        if ((value > low and value < high) and 
            self._isvalidBSTHelper(n.left,low,n.value) and
            self._isvalidBSTHelper(n.right,n.value,high)):
            return True
        return False
        
    def isValidBST(self,n):
        return self._isvalidBSTHelper(n,float('-inf'),float('inf'))
    
    
    
    
#Driver function
#           5
#          / \
#         4   7

node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))