class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        self.ans = set()
        self.dfs(k, n, [])
        return [x for x in self.ans]
        
    def dfs(self, k, curNum, usedNum:list):
        if k == 1:
            if curNum not in usedNum and 0 < curNum < 10:
                self.ans.add(tuple(sorted(usedNum+[curNum])))
        else:
            start = max(usedNum)+1 if usedNum else 1
            for i in range(start, 10):
                if curNum - i > 0:
                    usedNum.append(i)
                    self.dfs(k-1, curNum-i, usedNum)
                    usedNum.pop()