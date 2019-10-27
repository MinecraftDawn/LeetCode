class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i in s:
            ans *= 26
            ans += ord(i) - 64
            
        return ans