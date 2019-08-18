class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1+s2) != len(s3): return False
        s1 = 'a' + s1
        s2 = 'a' + s2
        s3 = 'aa' + s3
        dp = [[False] * (len(s1)+1) for _ in range(len(s2)+1)]
        dp[0][0] = True
        
        print(dp)
        
        for i in range(1, len(s1)+1):
            if s1[:i] == s3[:i]:
                dp[0][i] = True
                print(2)
                
        for i in range(1, len(s2)+1):
            if s2[:i] == s3[:i]:
                dp[i][0] == True
                print(1)
               
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[j][i] = (dp[j][i-1] and s1[i-1] == s3[i+j-1]) \
                or (dp[j-1][i] and s2[j-1] == s3[i+j-1])
               

        return dp[-1][-1]