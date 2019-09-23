class Solution:
    def minCut(self, s: str) -> int:
        s += ' '
        self.ans = []
        self.dfs(s, 0)
        
        return min(self.ans) - 1
    
    def dfs(self, s: str, length: int) -> list:            
        for i in range(1,len(s)):
            if self.isPalindrome(s[:i]):
                if i == len(s) - 1:
                    self.ans.append(length+1)
                else:
                    self.dfs(s[i:], length+1)
            
    def isPalindrome(self, s) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True