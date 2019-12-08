class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return ""
        
        def palindrome(s: str) -> bool:
            if s[:len(s)//2] == s[len(s)-len(s)//2:][::-1]:
                return True
            return False
        
        for i in range(len(s),-1,-1):
            if palindrome(s[:i]):
                return s[i:][::-1] + s