from itertools import permutations

class Solution:
    def permuteUnique(self, nums: list) -> list:
        res = list(permutations(nums,len(nums)))
        res = list(set(res))
        listRes = [list(tur) for tur in res]
        return listRes