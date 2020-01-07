from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sourceDict = defaultdict(int)
        for char in s:
            sourceDict[char] += 1
            
        for char in t:
            sourceDict[char] -= 1
            if sourceDict[char] == 0:
                sourceDict.pop(char)
            elif sourceDict[char] < 0:
                return False
            
            
        return not sourceDict.keys()