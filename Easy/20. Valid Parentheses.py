class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        
        stack = []
        symbolList = {'(':True,
                      '[':True,
                      '{':True,
                      ')':False,
                      ']':False,
                      '}':False}
        
        correSymbol = {')':'(',
                       ']':'[',
                       '}':'{'}
        
        for i in s:
            if symbolList.get(i):
                stack.append(i)
            else:
                if not stack: return False
                preSym = stack.pop()
                if correSymbol[i] != preSym:
                    return False
                
        if stack: return False
        
        return True 