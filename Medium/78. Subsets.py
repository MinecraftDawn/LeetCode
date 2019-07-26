from itertools import combinations
class Solution:
    def subsets(self, nums: list) -> list:
        ans = []
        for i in range(len(nums)+1):
            tmpAns = combinations(nums,i)
            for j in tmpAns:
                ans.append(list(j))
        return ans