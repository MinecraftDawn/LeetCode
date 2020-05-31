class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIndex = 0
        tIndex = 0
        while sIndex < len(s) and tIndex < len(t):
            sChar = s[sIndex]
            tChar = t[tIndex]
            if sChar == tChar:
                sIndex += 1
                tIndex += 1
            else:
                tIndex += 1

        return sIndex == len(s)