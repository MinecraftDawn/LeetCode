class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0: return ''
        prefix = ''
        minLength = len(strs[0])
        
        for string in strs:
            minLength = min(minLength,len(string))
            
        for i in range(minLength):
            char = strs[0][i]
            for j in strs:
                if char == j[i]:
                    pass
                else:
                    return prefix
            prefix += char
                
        return prefix