class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in hashmap:
                if i - hashmap[num] <= k:
                    return True
                else:
                    hashmap[num] = i
            else:
                hashmap[num] = i
                    
        return False