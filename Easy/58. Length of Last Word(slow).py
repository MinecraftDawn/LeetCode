class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ansList = s.split(' ')
        length = 0
        while ansList and length == 0:
            length = len(ansList.pop())
        return length