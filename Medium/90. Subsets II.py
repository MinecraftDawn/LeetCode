from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        ans = set()
        for i in range(len(nums)+1):
            for element in list(combinations(nums,i)):
                ans.add(tuple(sorted(element)))
        return ans