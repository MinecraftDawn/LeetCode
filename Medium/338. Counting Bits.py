class Solution:
    def countBits(self, num: int) -> list:
        ans = []
        for i in range(num+1):
            ans.append(bin(i).count("1"))
            
        return ans