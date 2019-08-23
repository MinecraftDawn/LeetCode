# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root: return []
        queue = []
        ans = []
        queue.append(root)
        
        count = [1,0]
        switch = False
        curLevel = []
        while queue:
            node = queue.pop(0)
            curLevel.append(node.val)
            count[switch] -= 1
            
            if node.left:
                queue.append(node.left)
                count[not switch] += 1
            if node.right:
                queue.append(node.right)
                count[not switch] += 1
                
            if not count[switch]:
                switch = not switch
                ans.append(curLevel)
                curLevel = []
                
        return ans