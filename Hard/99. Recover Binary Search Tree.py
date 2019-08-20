# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.nums = []
        self.nodes = []
        self.inorder(root)
        sortedNum = sorted(self.nums)
        
        for i in range(len(self.nums)):
            if sortedNum[i] != self.nums[i]:
                self.nodes[i].val = sortedNum[i]
            
        return self.nums
    
    def inorder(self, node:TreeNode):
        if not node: return
        
        self.inorder(node.left)
        self.nums.append(node.val)
        self.nodes.append(node)
        self.inorder(node.right)