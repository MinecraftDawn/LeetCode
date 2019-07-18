class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('/',' ')
        pathList = path.split()
        
        stack = []
        for i in pathList:
            if i == ".":
                pass
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
                
        if not stack:
            return '/'
    
        path = ""
        for i in stack:
            path += '/' + i
            
        return path