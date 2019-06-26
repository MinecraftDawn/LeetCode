from itertools import permutations

class Solution:
    def permute(self, nums: list) -> list:
        res = list(permutations(nums,len(nums)))
        listRes = [list(tur) for tur in res]
        return listRes