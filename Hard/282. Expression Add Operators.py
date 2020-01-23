# Reference: https://leetcode.com/problems/expression-add-operators/discuss/71900/18-line-clean-Python-solution-DFS-with-comment
class Solution:
    def addOperators(self, num: str, target: int) -> list:
        self.ans = []
        self.target = target
        self.calculate(num, "", 0, 0)
        return self.ans
        
    def calculate(self, num: str, curStr: str, curVal: int, pre:int):
        if not num:
            if curVal == self.target:
                self.ans.append(curStr)
        else:
            for i in range(1, len(num)+1):
                if i > 1 and num[0] == '0': continue
            
                if not curStr:
                    self.calculate(num[i:], num[:i], int(num[:i]), int(num[:i]))
                
                else:
                    self.calculate(num[i:], curStr + "+" + num[:i], curVal + int(num[:i]), int(num[:i]))
                    self.calculate(num[i:], curStr + "-" + num[:i], curVal - int(num[:i]), -int(num[:i]))
                    self.calculate(num[i:], curStr + "*" + num[:i], curVal - pre + pre * int(num[:i]), pre * int(num[:i]))