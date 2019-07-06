class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ansList = s.split()
        if not ansList:
            return 0
        
        return len(ansList[-1])