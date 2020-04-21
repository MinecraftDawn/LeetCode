class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        
        ans = 0
        for i in range(n, 0, -1):
            ans += self.countDigital(i)
        
        return ans
        
    def countDigital(self, n:int) -> int:
        if n == 1: return 10
        
        tmp = 9
        for i in range(9, 9-n+1, -1):
            tmp *= i
            
        return tmp