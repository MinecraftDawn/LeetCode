class Solution:
    def groupAnagrams(self, strs: list) -> list:
        myDir = {}
        
        for string in strs:
            key = ''.join(sorted(string))
            myDir[key] = myDir.get(key,[]) + [string]
        
        return list(myDir.values())