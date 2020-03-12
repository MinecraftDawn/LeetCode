class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#': return True
        
        preorder = preorder.split(",")
        stack = []
        
        for i,char in enumerate(preorder):
            if char == '#':
                if not stack: return False
                
                stack[-1] -= 1
                while stack[-1] == 0:
                    stack.pop()
                    if not stack:
                        if i != len(preorder) - 1: 
                            return False
                        else:
                            return True
                    
                    stack[-1] -= 1
            else:
                stack.append(2)
        
        return not stack