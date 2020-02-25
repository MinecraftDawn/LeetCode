class Solution:
    def bulbSwitch(self, n: int) -> int:
        n += 1
        ans = [True] * (n)
        for i in range(2, n):
            for j in range(0, n, i):
                ans[j] = not ans[j]
                
        return ans[1:].count(True)