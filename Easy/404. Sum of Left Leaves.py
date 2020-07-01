# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0

        ans = 0
        stack = [(root, False)]
        while stack:
            node, left = stack.pop()

            if not node.left and not node.right and left:
                ans += node.val
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))

        return ans