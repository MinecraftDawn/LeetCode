class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0: return 0
        
        ans = 1
        for i in range(2, n):
            if i*i <= n:
                ans += 1
                
        return ans