class Solution:
    def search(self, nums: list, target: int) -> bool:
        for i in nums:
            if target == i: return True
        return False