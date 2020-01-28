class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        strList = str.split()
        if len(strList) != len(pattern): return False
        
        for i in range(len(strList)):
            char = pattern[i]
            string = strList[i]
            if char in hashmap1:
                if string != hashmap1[char]:
                    return False
            else:
                hashmap1[char] = string
                
            if string in hashmap2:
                if char != hashmap2[string]:
                    return False
            else:
                hashmap2[string] = char
                
        return True