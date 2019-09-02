# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        if not root: return []
        stack = [[],[]]
        ans = []
        stack[0].append(root)
        
        switch = True
        curLevel = []
        while stack[0]:
            node = stack[0].pop()
            curLevel.append(node.val)
            
            if switch:
                if node.left:
                    stack[1].append(node.left)
                if node.right:
                    stack[1].append(node.right)
            else:
                if node.right:
                    stack[1].append(node.right)
                if node.left:
                    stack[1].append(node.left)
                
            if not stack[0]:
                switch = not switch
                stack[0],stack[1] = stack[1],stack[0]
                ans.append(curLevel)
                curLevel = []
                
        return ans