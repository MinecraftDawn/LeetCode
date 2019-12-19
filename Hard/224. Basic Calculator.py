class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]
        sign = 1
        
        index = 0
        while index < len(s):
            char = s[index]
            if char in ['+','-']:
                sign = 1 if char == '+' else -1     
                
            elif char.isdigit():
                tmp = index
                while index < len(s) and s[index].isdigit():
                    index += 1
                stack[-1] += sign * int(s[tmp:index])
                index -= 1
                
            elif char == "(":
                stack.append(sign)
                stack.append(0)
                sign = 1
                
            elif char == ")":
                num2 = stack.pop()
                num1 = stack.pop()
                stack[-1] += num1 * num2
                
            index += 1
            
        return stack[-1]