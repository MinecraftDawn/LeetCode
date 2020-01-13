class Solution:
    def __init__(self):
        self.ans = [1]
        self.count = self.two = self.three = self.five = 0
        
    def nthUglyNumber(self, n: int) -> int:
        while self.count < n:
            tmp = min((self.ans[self.two] * 2,
                      self.ans[self.three] * 3,
                      self.ans[self.five] * 5))
            
            if tmp == self.ans[self.two] * 2:
                self.two += 1
            elif tmp == self.ans[self.three] * 3:
                self.three += 1
            else:
                self.five += 1
                
            if tmp == self.ans[-1]: continue
            
            self.ans.append(tmp)
            self.count += 1
            
        return self.ans[n-1]