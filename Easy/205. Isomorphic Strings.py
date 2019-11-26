class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        map1 =  {}
        map2 = {}
        for i in range(len(s)):
            if s[i] in map1:
                if map1[s[i]] != t[i]:
                    return False
            else:
                map1[s[i]] = t[i]
            if t[i] in map2:
                if map2[t[i]] != s[i]:
                    return False
            else:
                map2[t[i]] = s[i]
        return True