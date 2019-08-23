# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue
class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root: return []
        queue = Queue()
        ans = []
        queue.put(root)
        
        count = [1,0]
        switch = False
        curLevel = []
        while not queue.empty():
            node = queue.get()
            curLevel.append(node.val)
            count[switch] -= 1
            
            if node.left:
                queue.put(node.left)
                count[not switch] += 1
            if node.right:
                queue.put(node.right)
                count[not switch] += 1
                
            if not count[switch]:
                switch = not switch
                ans.append(curLevel)
                curLevel = []
                
        return ans
        