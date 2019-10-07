class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        self.ans = []
        self.preorder(root)
        return self.ans
    
    def preorder(self, node:TreeNode):
        if not node: return
        
        self.ans.append(node.val)
        self.preorder(node.left)
        self.preorder(node.right)