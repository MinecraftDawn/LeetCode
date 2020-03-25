class Solution:
    def countBits(self, num: int) -> list:
        ans = [0]
        for i in range(1, num+1):
            ans.append(ans[i>>1] + (i&1))
            
        return ans