# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        self.valid = True
        
        self.comparisonNode(root.left, root.right)
        
        return self.valid
        
    
    def comparisonNode(self, node1:TreeNode, node2:TreeNode):
        if self.valid:
            if not node1 and not node2:
                return
            elif node1 and node2:
                if node1.val == node2.val:
                    self.comparisonNode(node1.left, node2.right)
                    self.comparisonNode(node1.right, node2.left)
                else:
                    self.valid = False
            else:
                self.valid = False