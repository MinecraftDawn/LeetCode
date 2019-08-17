class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.ans = False
        self.recursive(s1,s2,s3)
        return self.ans
        
        
    def recursive(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            self.ans = True
            return True
        
        if not self.ans:
            if s3:
                if s1:
                    if s1[0] == s3[0]:
                        self.recursive(s1[1:],s2,s3[1:])
                if s2:
                    if s2[0] == s3[0]:
                        self.recursive(s1,s2[1:],s3[1:])