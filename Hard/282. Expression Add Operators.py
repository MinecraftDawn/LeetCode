class Solution:
    def addOperators(self, num: str, target: int) -> list:
        self.ans = []
        self.target = target
        self.calculate(num, 1)
        return self.ans
        
    def calculate(self, num: str, pos:int):
        if pos >= len(num):
            try:
                if eval(num) == self.target:
                    self.ans.append(num)
            except:
                pass
        else:
            self.calculate(num[:pos] + "+" + num[pos:], pos+2)
            self.calculate(num[:pos] + "-" + num[pos:], pos+2)
            self.calculate(num[:pos] + "*" + num[pos:], pos+2)
            if pos+1 < len(num) and num[pos+1] != '0':
                self.calculate(num[:pos] + num[pos:], pos+1)