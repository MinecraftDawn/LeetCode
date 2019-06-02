class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if not words: return []
        findIndex = []
        wordLen = len(words[0])
        
        for i in range(len(s) - len(words) * wordLen+1):
            tmpWorlds = words.copy()
            
            for j in range(len(words)):
                string = s[i+j*wordLen:i+(j+1)*wordLen]
                if string in tmpWorlds:
                    tmpWorlds.remove(string)
                else: break
            
            if not tmpWorlds:
                findIndex.append(i)
            
        return findIndex