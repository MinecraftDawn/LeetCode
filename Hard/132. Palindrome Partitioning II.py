# Reference : https://www.cnblogs.com/grandyang/p/4271456.html
class Solution:
    def minCut(self, s: str) -> int:
        if not s: return 0
        # 儲存是否回文
        dp = [[False] * len(s) for _ in s]
        # 總共要切幾段
        cut = [0] * len(s)
        
        for i in range(len(s)):
            # 前i部分最多切i段
            cut[i] = i
            for j in range(0, i+1):
                # 如果有回文
                if s[i] == s[j] and (i-j < 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    # 若有回文，則段數可沿用前一個
                    cut[i] = 0 if j==0 else min(cut[i], cut[j-1] + 1)
        return cut[-1]