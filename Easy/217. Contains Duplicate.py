class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i] = True