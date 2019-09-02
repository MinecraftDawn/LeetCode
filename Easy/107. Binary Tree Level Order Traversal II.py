# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root: return []
        queue = [[],[]]
        ans = []
        queue[0].append(root)
        
        curLevel = []
        while queue[0]:
            node = queue[0].pop(0)
            curLevel.append(node.val)
            
            if node.left:
                queue[1].append(node.left)
            if node.right:
                queue[1].append(node.right)
                
            if not queue[0]:
                queue[0],queue[1] = queue[1],queue[0]
                ans.append(curLevel)
                curLevel = []
                
        ans.reverse()
        return ans