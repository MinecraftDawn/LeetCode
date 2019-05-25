class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLength = len(s)
        
        maxStr = ''
        for i in range(strLength):
            currentStr = ''
            for j in range(i, strLength):
                if currentStr.find(s[j]) >= 0:
                    break
                else:
                    currentStr += s[j]
                
            if len(currentStr) > len(maxStr) :
                maxStr = currentStr
                
        return len(maxStr)