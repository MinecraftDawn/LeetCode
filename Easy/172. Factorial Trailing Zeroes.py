class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5: return 0
        
        ans = 0
        while n >= 5:
            n = n // 5
            ans += n
            
        return ans