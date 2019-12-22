from operator import add,sub,mul,floordiv
class Solution:
    def calculate(self, s: str) -> int:
        numStack = []
        operStack = []
        
        operFunc = {'+':add,
                    '-':sub,
                    '*':mul,
                    '/':floordiv}
        
        index = 0
        while index < len(s):
            char = s[index]
            if char in ['+','-','*','/']:
                if not operStack:
                    operStack.append(char)
                else:
                    if self.getPriority(char) > self.getPriority(operStack[-1]):
                        operStack.append(char)
                    else:
                        while operStack and self.getPriority(char) <= self.getPriority(operStack[-1]):
                            num2 = numStack.pop()
                            num1 = numStack.pop()
                            cacul = operFunc[operStack.pop()](num1,num2)
                            numStack.append(cacul)
                        operStack.append(char)
                    
            elif char.isdigit():
                tmp = index
                while index < len(s) and s[index].isdigit():
                    index += 1
                numStack.append(int(s[tmp:index]))
                index -= 1
                
            index += 1
            
            
        while operStack:
            num2 = numStack.pop()
            num1 = numStack.pop()
            cacul = operFunc[operStack.pop()](num1,num2)
            numStack.append(cacul)
        
        return numStack.pop()
    def getPriority(self, char):
        if char in ['+','-']:
            return 1
        else:
            return 2