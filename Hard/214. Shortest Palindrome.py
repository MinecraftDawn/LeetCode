class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return ""
        
        for i in range(len(s),-1,-1):
            sub = s[:i]
            if sub == sub[::-1]:
                return s[len(sub):][::-1] + s