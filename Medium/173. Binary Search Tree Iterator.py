# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.curNode = root
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.curNode or self.stack:
            if self.curNode:
                self.stack.append(self.curNode)
                self.curNode = self.curNode.left
            elif self.stack:
                self.curNode = self.stack.pop()
                returnNode = self.curNode
                self.curNode = self.curNode.right 
                return returnNode.val
        return None

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.curNode or self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()