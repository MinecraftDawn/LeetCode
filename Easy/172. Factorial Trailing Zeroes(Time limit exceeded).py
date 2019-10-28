class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 1
        for i in range(1,n+1):
            num *= i
            
        ans = 0
        while num % 10 == 0:
            num //= 10
            ans += 1
            
        return ans