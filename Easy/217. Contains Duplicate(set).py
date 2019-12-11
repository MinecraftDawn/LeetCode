class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        numSet = set()
        for i in nums:
            if i in numSet:
                return True
            else:
                numSet.add(i)