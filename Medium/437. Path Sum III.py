# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def __init__(self):
        self.ans = 0
        self.pathVal = defaultdict(int)
        self.pathVal[0] = 1

    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root: return 0

        self.target = target
        self.dfs(root, 0)

        return self.ans

    def dfs(self, node: TreeNode, val: int):
        curVal = val + node.val
        self.ans += self.pathVal[curVal - self.target]
        self.pathVal[curVal] += 1
        if node.left: self.dfs(node.left, curVal)
        if node.right: self.dfs(node.right, curVal)
        self.pathVal[curVal] -= 1