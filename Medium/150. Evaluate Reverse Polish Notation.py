from operator import add, sub, mul

def myDiv(num1, num2):
    return int(num1/num2)

class Solution:
    def evalRPN(self, tokens: list) -> int:
        operand = []
        operatorDict = {'+':add,
                        '-':sub,
                        '*':mul,
                        '/':myDiv}
        
        for i in tokens:
            if i in operatorDict:
                if operand:
                    num2 = operand.pop()
                    num1 = operand.pop()
                    
                    operand.append(operatorDict[i](num1,num2))
                else:
                    pass
            else:
                operand.append(int(i))
        
        return operand.pop()