class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        while n:
            n -= 1
            
            mod = n%26
            ans = chr(mod + 65) + ans
            
            n //= 26
        return ans