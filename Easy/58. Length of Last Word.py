class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        firstSpace = True
        length = 0
        for i in range(len(s)-1,-1,-1):
            if firstSpace and s[i] == ' ':
                continue
            else:
                if s[i] == ' ': break
                firstSpace = False
                length += 1
        return length