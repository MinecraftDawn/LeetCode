# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root: return 0

        self.nodes = []
        self.target = target
        self.burst(root, 0)

        for node in self.nodes[1:]:
            self.burst(node, 0)

        return self.ans

    def burst(self, node: TreeNode, val: int):
        self.nodes.append(node)
        curVal = val + node.val
        if curVal == self.target:
            self.ans += 1

        if node.left:
            self.burst(node.left, curVal)
        if node.right:
            self.burst(node.right, curVal)