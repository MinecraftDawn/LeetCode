class Solution:
    def partition(self, s: str) -> list:
        s+=' '
        self.ans = []
        self.dfs(s, [])
        
        return self.ans
    
    def dfs(self, s: str, partition: list) -> list:            
        for i in range(1,len(s)):
            if self.isPalindrome(s[:i]):
                p = partition.copy()
                p.append(s[:i])
                if i == len(s) - 1:
                    self.ans.append(p)
                else:
                    self.dfs(s[i:], p)
            
    def isPalindrome(self, s) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True