class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2): return False
        
        length = len(s1)
        if length == 1:
            if s1 == s2: return True
            else: return False
        
        for i in range(1,length):
            if self.isScramble(s1[i:],s2[:-i]) and self.isScramble(s1[:i],s2[-i:]):
                return True
            elif self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            
        return False